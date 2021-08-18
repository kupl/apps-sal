class Solution:
    def search(self, S, mid) -> str:
        n = len(S)
        self.nums = [ord(S[i]) - ord('a') for i in range(n)]
        base = 26
        MOD = 2**32

        hash_ = 0
        for i in range(mid):
            hash_ = (hash_ * base + self.nums[i]) % MOD

        visited = {hash_}
        aL = pow(base, mid, MOD)
        for start in range(1, n - mid + 1):
            hash_ = (hash_ * base - self.nums[start - 1] * aL + self.nums[start + mid - 1]) % MOD
            if hash_ in visited:
                return start
            visited.add(hash_)
        return -1

    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        self.nums = [ord(S[i]) - ord('a') for i in range(n)]
        base = 26
        MOD = 2**32

        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if self.search(S, mid) != -1:
                left = mid + 1
            else:
                right = mid - 1

        start = self.search(S, left - 1)
        return S[start: start + left - 1]
