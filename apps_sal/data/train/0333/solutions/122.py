class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # dp (forward backward pass) didn't work
        # from solution, do bfs
        # but add mirror positions as neighbors
        n = len(arr)

        mirrors = collections.defaultdict(list)
        _ = [mirrors[x].append(i) for i, x in enumerate(arr)]

        visited = set()
        q = collections.deque([(0, 0)])
        while q:
            idx, jump = q.popleft()
            if idx == n - 1:
                return jump

            for nei in [idx - 1, idx + 1] + mirrors[arr[idx]]:
                if 0 <= nei < n and nei not in visited:
                    visited.add(nei)
                    q.append((nei, jump + 1))
            del mirrors[arr[idx]]  # dont consider it from its neighbors again
