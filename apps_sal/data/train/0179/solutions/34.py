from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def _len(cnt): return 1 if cnt == 1 else 2 if cnt <= 9 else 3 if cnt <= 99 else 4

        @lru_cache(None)
        def solve(left, k):
            if k < 0:
                return float('inf')
            if left + 1 == k:
                return 0
            res = min(solve(left - 1, k) + 1, solve(left - 1, k - 1))
            cnt = 1
            for j in range(left - 1, -1, -1):
                if s[j] != s[left]:
                    k -= 1
                    if k < 0:
                        break
                else:
                    cnt += 1
                    if j < k:
                        break
                    res = min(res, solve(j - 1, k) + _len(cnt))
            return res
        return solve(len(s) - 1, k)
