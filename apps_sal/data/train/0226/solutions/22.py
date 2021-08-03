from collections import Counter


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:

        counts = Counter(A)
        graph = {x: [] for x in counts}

        for x in counts:
            for y in counts:
                r = int((x + y) ** 0.5 + 0.5)
                if r * r == x + y:
                    graph[x].append(y)

        def dfs(x, todo):
            counts[x] -= 1
            if todo == 0:
                res = 1
            else:
                res = 0
                for y in graph[x]:
                    if counts[y] > 0:
                        res += dfs(y, todo - 1)

            counts[x] += 1
            return res

        return sum(dfs(x, len(A) - 1) for x in counts)
