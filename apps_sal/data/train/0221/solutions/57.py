class Solution:
    def longestDupSubstring(self, S: str) -> str:
        self.A = [ord(c) - ord('a') for c in S]

        start, end = 1, len(S)
        while start + 1 < end:
            mid = (start + end) // 2
            pos = self.check(mid)
            if pos:
                start = mid
            else:
                end = mid

        pos = self.check(end)
        if pos:
            return S[pos: pos + end]
        pos = self.check(start)
        if pos:
            return S[pos: pos + start]
        return ''

    def check(self, length):
        mod = 2**63 - 1
        power = pow(26, length, mod)

        cur = 0
        for i in range(length):
            cur = (cur * 26 + self.A[i]) % mod

        # cur = reduce(lambda x, y: (x * 26 + y) % mod, self.A[:length], 0)
        seen = {cur}

        for i in range(length, len(self.A)):
            cur = (cur * 26 + self.A[i] - self.A[i - length] * power) % mod
            if cur in seen:
                return i - length + 1
            seen.add(cur)
