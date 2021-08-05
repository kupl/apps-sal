class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        def edge(x, y):
            return int((x + y) ** 0.5) ** 2 == (x + y)

        def dfs(x, t):
            count[x] -= 1
            if t == 0:
                ans = 1
            else:
                ans = 0
                for y in graph[x]:
                    if count[y]:
                        ans += dfs(y, t - 1)
            count[x] += 1
            return ans

        N = len(A)
        count = collections.Counter(A)
        graph = collections.defaultdict(list)
        for x in count:
            for y in count:
                if edge(x, y):
                    graph[x].append(y)

        return sum(dfs(x, N - 1) for x in count)
