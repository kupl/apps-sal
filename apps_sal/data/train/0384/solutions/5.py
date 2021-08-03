class Solution:

    BASE = 10 ** 9 + 7

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        total_cnt = 0
        total_prod = 0
        ans = 0
        for num in A:
            ans = (ans + total_cnt * num - total_prod) % self.BASE
            total_cnt = (2 * total_cnt + 1) % self.BASE
            total_prod = (2 * total_prod + num) % self.BASE
        return ans
