class Solution:
    def clumsy(self, N: int) -> int:
        ans = self.multiplyDivide(N)
        N -= 3
        while N > 0:
            ans += max(N, 0)
            ans -= self.multiplyDivide(N - 1)
            N -= 4
        return ans

    def multiplyDivide(self, n: int) -> int:
        return max(0, n) * max(1, n - 1) // max(1, n - 2)
