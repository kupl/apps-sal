class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        bfs = []
        heapq.heappush(bfs, (0, 0))
        seen = {}
        seen[0] = 0
        G = defaultdict(list)
        for (i, a) in enumerate(arr):
            G[a].append(i)
        while bfs:
            (step, idx) = heapq.heappop(bfs)
            idx = -idx
            for d in (-1, 1):
                nidx = idx + d
                if nidx >= 0 and nidx < len(arr):
                    if nidx not in seen or seen[nidx] > step + 1:
                        if nidx == len(arr) - 1:
                            return step + 1
                        seen[nidx] = step + 1
                        heapq.heappush(bfs, (step + 1, -nidx))
            for d in G[arr[idx]][::-1]:
                if d not in seen or seen[d] > step + 1:
                    if d == len(arr) - 1:
                        return step + 1
                    seen[d] = step + 1
                    heapq.heappush(bfs, (step + 1, -d))
        return -1
