class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = collections.defaultdict(list)
        time = {}
        for i, (m, t) in enumerate(zip(manager, informTime)):
            tree[m].append(i)
            time[i] = t

        ans = 0

        def dfs(node, t):
            nonlocal ans

            t += time[node]
            for child in tree[node]:
                dfs(child, t)
            ans = max(ans, t)

        dfs(headID, 0)
        return ans
