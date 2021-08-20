class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def method1():

            def dfs(node, time):
                nonlocal ans
                if not children[node]:
                    ans = max(ans, time)
                    return
                for c in children[node]:
                    dfs(c, time + informTime[node])
            children = [[] for i in range(n)]
            for (i, m) in enumerate(manager):
                if m >= 0:
                    children[m].append(i)
            ans = float('-inf')
            dfs(headID, 0)
            return ans
        return method1()

        def method2():
            children = [[] for i in range(n)]
            for (i, m) in enumerate(manager):
                if m >= 0:
                    children[m].append(i)

            def dfs(i):
                return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
            return dfs(headID)
        return method2()
