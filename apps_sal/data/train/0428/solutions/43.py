from collections import defaultdict, deque
import heapq, itertools

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # Brute Force + Permutations
        # Time  complexity: O(R x C x A x A!), where R, C are the dimensions of the grid,
        # and A is the maximum number of keys.
        # Space compleixty: O(R x C + A!)
        # R, C = map(len, (grid, grid[0]))
        # location = {v: (r, c)
        #             for r, row in enumerate(grid)
        #             for c, v in enumerate(row)
        #             if v not in '.#'}

        # def neighbors(r, c):
        #     for cr, cc in (r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1):
        #         if 0 <= cr < R and 0 <= cc < C:
        #             yield cr, cc

        # def bfs(source, target, keys=()):
        #     sr, sc = location[source]
        #     tr, tc = location[target]
        #     seen = [[False] * C for _ in range(R)]
        #     seen[sr][sc] = True
        #     queue = deque([(sr, sc, 0)])
        #     while queue:
        #         r, c, d = queue.popleft()
        #         if r == tr and c == tc: return d
        #         for cr, cc in neighbors(r, c):
        #             if not seen[cr][cc] and grid[cr][cc] != '#':
        #                 if grid[cr][cc].isupper() and grid[cr][cc].lower() not in keys:
        #                     continue
        #                 queue.append((cr, cc, d + 1))
        #                 seen[cr][cc] = True
        #     return float(\"inf\")

        # ans = float(\"inf\")
        # keys = \"\".join(chr(ord('a') + i) for i in range(len(location) // 2))
        # for cand in itertools.permutations(keys):
        #     bns = 0
        #     for i, target in enumerate(cand):
        #         source = cand[i - 1] if i > 0 else '@'
        #         d = bfs(source, target, cand[:i])
        #         bns += d
        #         if bns >= ans: break
        #     else:
        #         ans = bns

        # return ans if ans < float(\"inf\") else -1



        # Points of Interest + Dijkstra
        # Time  complexity: O(RC(2A + 1) + ElogN), where R, C are the dimensions of the grid, 
        # and A is the maximum number of keys, N = (2A + 1) x 2^A is the number of nodes when we
        # perform Dijkstra's, and E = N x (2A + 1) is the maximum number of edges.
        # Space complexity: ON(N)
        R, C = len(grid), len(grid[0])

        # The points of interest
        location = {v: (r, c)
                    for r, row in enumerate(grid)
                    for c, v in enumerate(row)
                    if v not in '.#'}

        def neighbors(r, c):
            for cr, cc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        # The distance from source to each point of interest
        def bfs_from(source):
            r, c = location[source]
            seen = [[False] * C for _ in range(R)]
            seen[r][c] = True
            queue = deque([(r, c, 0)])
            dist = {}
            while queue:
                r, c, d = queue.popleft()
                if source != grid[r][c] != '.':
                    dist[grid[r][c]] = d
                    continue # Stop walking from here if we reach a point of interest
                for cr, cc in neighbors(r, c):
                    if grid[cr][cc] != '#' and not seen[cr][cc]:
                        seen[cr][cc] = True
                        queue.append((cr, cc, d + 1))
            return dist        

        dists = {place: bfs_from(place) for place in location}
        target_state = 2 ** sum(p.islower() for p in location) - 1

        #Dijkstra
        pq = [(0, '@', 0)]
        final_dist = defaultdict(lambda: float('inf'))
        final_dist['@', 0] = 0
        while pq:
            d, place, state = heapq.heappop(pq)
            if final_dist[place, state] < d: continue
            if state == target_state: return d
            for destination, d2 in list(dists[place].items()):
                state2 = state
                if destination.islower(): #key
                    state2 |= 1 << ord(destination) - ord('a')
                elif destination.isupper(): #lock
                    if not(state & (1 << ord(destination) - ord('A'))): #no key
                        continue

                if d + d2 < final_dist[destination, state2]:
                    final_dist[destination, state2] = d + d2
                    heapq.heappush(pq, (d + d2, destination, state2))

        return -1

