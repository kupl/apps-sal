class Solution:
    def minDays(self, n: int) -> int:
        #         Iterative DFS(Time Limit Exceded)

        #         stack = [(n, 0)]
        #         minDays = float('inf')
        #         seen = {}
        #         while stack:
        #             numOrgs, curDays = stack.pop()

        #             if numOrgs == 0:
        #                 minDays = min(minDays, curDays)
        #                 continue

        #             if numOrgs < 0:
        #                 continue

        #             stack.append((numOrgs - 1, curDays + 1))

        #             if numOrgs % 2 == 0:
        #                 stack.append((numOrgs - (numOrgs // 2), curDays + 1))

        #             if numOrgs % 3 == 0:
        #                 stack.append((numOrgs - 2 * (numOrgs // 3), curDays + 1))

        #         return minDays

        #         DFS with cache(reached max depth)

        #         def dfs(numOrngs):
        #             if numOrngs in seen:
        #                 return seen[numOrngs]

        #             if numOrngs == 0:
        #                 return 1

        #             if numOrngs < 0:
        #                 return float('inf')

        #             a = dfs(numOrngs - 1)

        #             b = float('inf')
        #             if numOrngs % 2 == 0:
        #                 b = dfs(numOrngs - (numOrngs // 2))

        #             c = float('inf')
        #             if numOrngs % 3 == 0:
        #                 c = dfs(numOrngs - 2 * (numOrngs // 3))

        #             seen[numOrngs] = min(a, b, c) + 1

        #             return seen[numOrngs]

        #         seen = {}
        #         return dfs(n) - 1

        def dfs(numOrngs):

            if numOrngs in seen:
                return seen[numOrngs]

            if numOrngs == 0:
                return 0

            if numOrngs < 0:
                return float('inf')

            seen[numOrngs] = min((numOrngs % 2) + dfs(numOrngs // 2), (numOrngs % 3) + dfs(numOrngs // 3)) + 1

            return seen[numOrngs]

        seen = {}
        return dfs(n) - 1
