class Solution:

    def tallestBillboard(self, rods):
        mem = {}

        def dp(i, s):
            if (i, s) in mem:
                return mem[i, s]
            if i == len(rods):
                return 0 if s == 0 else float('-inf')
            res = max(dp(i + 1, s), dp(i + 1, s - rods[i]), dp(i + 1, s + rods[i]) + rods[i])
            mem[i, s] = res
            return res
        return dp(0, 0)
