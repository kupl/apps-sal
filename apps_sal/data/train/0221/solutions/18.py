class Solution:

    def longestDupSubstring(self, S: str) -> str:
        lo = 1
        hi = len(S)
        nums = [ord(i) - ord('a') for i in S]
        self.modulus = 2 ** 32

        def dup(l):
            seen = set()
            hval = 0
            for i in range(l):
                hval = (hval * 26 + nums[i]) % self.modulus
            seen.add(hval)
            al = pow(26, l, self.modulus)
            for i in range(1, len(S) - l + 1):
                hval = (hval * 26 - nums[i - 1] * al + nums[i + l - 1]) % self.modulus
                if hval in seen:
                    return i
                seen.add(hval)
            return -1
        start = -1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            begin = dup(mi)
            if begin != -1:
                lo = mi + 1
                start = begin
            else:
                hi = mi - 1
        return S[start:start + lo - 1]
