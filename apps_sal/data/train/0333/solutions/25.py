class Solution:

    def minJumps(self, a: List[int]) -> int:
        n = len(a)
        adj = defaultdict(list)
        for (i, x) in enumerate(a):
            adj[x].append(i)
        q = [(0, 0)]
        seen = [False] * n
        seen[0] = True
        for (u, d) in q:
            if u == n - 1:
                return d
            for v in (u - 1, u + 1):
                if 0 <= v < n and (not seen[v]):
                    seen[v] = True
                    q.append((v, d + 1))
            x = a[u]
            for v in adj[x]:
                if not seen[v]:
                    seen[v] = True
                    q.append((v, d + 1))
            if adj[x]:
                adj[x] = []
