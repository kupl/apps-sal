class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # if lo == hi:
        #   return lo

        ans = []
        for i in range(lo, hi + 1):
            num = i
            ctr = 0
            while num != 1:
                if num % 2 != 0:  # odd
                    num = (num * 3) + 1
                else:
                    num = num / 2
                ctr += 1
            ans.append((ctr, i))

        return sorted(ans, key=lambda x: x[0])[k - 1][1]
