class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        size = len(A)
        mod = 10 ** 9 + 7
        pow_mod = [1] * size
        for i in range(1, size):
            pow_mod[i] = (pow_mod[i - 1] * 2) % mod

        A.sort()
        ans = 0
        for i in range(size):
            ans += (A[i] * ((pow_mod[i] - pow_mod[size - 1 - i]) % mod)) % mod
            ans %= mod
        return ans
