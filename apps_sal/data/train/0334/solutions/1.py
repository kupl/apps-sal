class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        idx = []
        res = 0
        for i in range(n):
            if idx and s[i] == s[idx[-1]]:
                cost_cur = cost[i]
                cost_pre = cost[idx[-1]]
                if cost_cur > cost_pre:
                    res += cost_pre
                    idx.pop()
                    idx.append(i)
                else:
                    res += cost_cur
            else:
                idx.append(i)
        return res
