from collections import defaultdict
from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # char2ids = defaultdict(list)
        # for i, c in enumerate(s):
        #     if len(char2ids[c]) == 0 or i > char2ids[c][-1] + 1:
        #         char2ids[c].append(i)

        def compressed_length(cnt):
            return 4 if cnt == 100 else (3 if cnt >= 10 else (2 if cnt > 1 else 1))

        @lru_cache(None)
        def DP(i, k):
            if k < 0: return float('inf')
            if i + 1 <= k: return 0

            ret = min(DP(i - 1, k) + 1, DP(i - 1, k - 1))
            cnt = 1
            for j in range(i - 1, -1, -1):
                if s[j] != s[i]:
                    k -= 1
                    if k < 0: break
                else:
                    cnt += 1
                    ret = min(DP(j - 1, k) + compressed_length(cnt), ret)

            return ret

        return DP(len(s) - 1, k)
