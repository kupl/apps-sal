class Solution:
    def longestDupSubstring(self, S: str) -> str:
        base, mod = 26, 2**63 - 1
        n = len(S)
        A = [ord(ch) - ord('a') for ch in S]

        def k_dup(k):
            curr = 0
            for i in range(k):
                curr = (curr * base + A[i]) % mod
            seen = {curr}
            for i in range(1, n - k + 1):
                curr = (base * curr - pow(base, k, mod) * A[i - 1] + A[i + k - 1]) % mod
                if curr in seen:
                    return i
                seen.add(curr)
            return 0
        l, r, ans = 0, n, 0
        while l < r:
            mid = (l + r + 1) >> 1
            pos = k_dup(mid)
            # print(pos, mid)
            if pos:
                l = mid
                ans = pos
            else:
                r = mid - 1
        return S[ans:ans + l]
