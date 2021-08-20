class Solution:

    def longestDupSubstring(self, S: str) -> str:

        def check(sz):
            seen = defaultdict(list)
            (cur, base, MOD) = (0, 256, (1 << 31) - 1)
            h = (1 << sz * 8) % MOD
            for i in range(sz):
                cur *= base
                cur += ord(S[i])
                cur %= MOD
            seen[cur].append(0)
            for i in range(sz, len(S)):
                cur *= base
                cur += ord(S[i])
                cur -= ord(S[i - sz]) * h
                cur %= MOD
                for j in seen[cur]:
                    if S[j:j + sz] == S[i - sz + 1:i + 1]:
                        return (True, S[i - sz + 1:i + 1])
                seen[cur].append(i - sz + 1)
            return (False, '')
        (lo, hi) = (1, len(S))
        res = ''
        while lo <= hi:
            mid = (lo + hi) // 2
            (flag, tmp) = check(mid)
            if flag:
                lo = mid + 1
                res = tmp
            else:
                hi = mid - 1
        return res
