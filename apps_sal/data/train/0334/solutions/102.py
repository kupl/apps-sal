class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        pre = None
        val = 0
        ans = 0
        for e, v in zip(s, cost):
            if pre == e:
                ans += min(v, val)
                val = max(v, val)
            else:
                pre, val = e, v
        return ans
