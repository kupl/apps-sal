class Solution:

    def search(self, L: int, base: int, MOD: int, n: int, nums: List[int]) -> str:
        h = 0
        for i in range(L):
            h = (h * base + nums[i]) % MOD
        seen = {h}
        aL = pow(base, L, MOD)
        for start in range(1, n - L + 1):
            h = (h * base - nums[start - 1] * aL + nums[start + L - 1]) % MOD
            if h in seen:
                return start
            seen.add(h)
        return -1

    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        base = 26
        MOD = 2 ** 32
        (left, right) = (1, n)
        while left <= right:
            mid = left + (right - left) // 2
            if self.search(mid, base, MOD, n, nums) != -1:
                left = mid + 1
            else:
                right = mid - 1
        start = self.search(left - 1, base, MOD, n, nums)
        return S[start:start + left - 1]
