class Solution:

    def catMouseGame(self, graph: List[List[int]]) -> int:

        def encode(p, c, m):
            return c << 7 | m << 1 | p

        def decode(c):
            return (c & 1, c >> 7, c >> 1 & 63)
        n = len(graph)
        g = collections.defaultdict(list)
        outcomes = {}
        degrees = collections.Counter()
        for c in range(1, n):
            for m in range(n):
                for p in range(2):
                    status = encode(p, c, m)
                    if p == 0:
                        if c == m:
                            outcomes[status] = 1
                        elif m == 0:
                            outcomes[status] = -1
                    elif m == 0:
                        outcomes[status] = 1
                    elif c == m:
                        outcomes[status] = -1
                    if outcomes.get(status, 0):
                        continue
                    if p == 0:
                        for i in graph[c]:
                            if i == 0:
                                continue
                            st = encode((p + 1) % 2, i, m)
                            g[st].append(status)
                            degrees[status] += 1
                    else:
                        for i in graph[m]:
                            st = encode((p + 1) % 2, c, i)
                            g[st].append(status)
                            degrees[status] += 1

        def dfs(status):
            visited.add(status)
            for st in g[status]:
                if st not in visited:
                    if outcomes[status] == -1:
                        outcomes[st] = 1
                    else:
                        degrees[st] -= 1
                        if degrees[st] == 0:
                            outcomes[st] = -1
                        else:
                            continue
                    dfs(st)
        visited = set()
        for c in range(1, n):
            for m in range(n):
                for p in range(2):
                    st = encode(p, c, m)
                    if outcomes.get(st, 0) and st not in visited:
                        dfs(st)
        o = outcomes.get(encode(1, 2, 1), 0)
        if o == -1:
            o = 2
        return o
