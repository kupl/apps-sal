from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def _len(cnt): return 1 if cnt == 1 else 2 if cnt <= 9 else 3 if cnt <= 99 else 4

        @lru_cache(None)
        def solve(left, k):
            if k < 0:
                return float('inf')
            # remove s[0:left+1]
            if left + 1 == k:
                #                 print(93, left -1, k )
                return 0
            # 1. keep s[left], regard no repeating
            # 2. remove s[left]
            res = min(solve(left - 1, k) + 1, solve(left - 1, k - 1))
#             print(98, left -1, k )
            # 3. fix repeating characters
            cnt = 1
            for j in range(left - 1, -1, -1):
                if j < k:
                    break
                elif s[j] != s[left]:
                    k -= 1
                else:
                    cnt += 1
                    res = min(res, solve(j - 1, k) + _len(cnt))
#                 print(110, j -1, k )
            return res
        return solve(len(s) - 1, k)
