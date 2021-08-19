class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}

        def num_steps(num):
            if num == 1:
                return 0
            elif num in memo:
                return memo[num]
            if num % 2 == 0:
                memo[num] = num_steps(num / 2) + 1
            else:
                memo[num] = num_steps(num * 3 + 1) + 1
            return memo[num]
        vals = []
        for i in range(lo, hi + 1):
            vals.append((i, num_steps(i)))
        vals = sorted(vals, key=lambda x: (x[1], x[0]))
        print(vals)
        vals = [i for (i, j) in vals]
        return vals[k - 1]
