class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def method1():
            def dfs(node, time):
                nonlocal ans
                if node not in set(manager):
                    ans = max(ans, time)
                    return

                for i, m in enumerate(manager):
                    if m == node:
                        dfs(i, time + informTime[m])

            ans = float('-inf')
            dfs(headID, 0)
            return ans

        def method2():
            children = [[] for i in range(n)]
            for i, m in enumerate(manager):
                if m >= 0:
                    children[m].append(i)

            def dfs(i):
                return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
            return dfs(headID)

        return method2()
