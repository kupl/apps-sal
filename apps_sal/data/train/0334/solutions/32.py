class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        mx = ans = 0
        p = ''
        for (i, (x, c)) in enumerate(zip(s, cost)):
            ans += c
            if p != x:
                ans -= mx
                mx = 0
                p = x
            if c > mx:
                mx = c
        return ans - mx
