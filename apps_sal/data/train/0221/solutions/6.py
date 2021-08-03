from functools import reduce


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        def isDuplicate(len_s):
            p = pow(31, len_s, mod)
            seen = collections.defaultdict(list)
            cur = reduce(lambda x, y: (x * 31 + y) % mod, A[:len_s])
            seen[cur].append(0)
            for j in range(1, len(A) - len_s + 1):
                cur = (cur * 31 - A[j - 1] * p + A[j + len_s - 1]) % mod
                if cur in seen:
                    for i in seen[cur]:
                        if S[i:i + len_s] == S[j:j + len_s]:
                            return j
                seen[cur].append(j)
            return 0

        l, r = 1, len(S) - 1
        ans = ''
        while l <= r:
            mid = l + (r - l) // 2
            pos = isDuplicate(mid)
            if pos:
                ans = S[pos:pos + mid]
                l = mid + 1
            else:
                r = mid - 1
        return ans
