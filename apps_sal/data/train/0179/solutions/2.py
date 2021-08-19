from typing import *
from functools import lru_cache


class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        def get_compressed_len(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return len(str(n)) + 1

        @lru_cache(None)
        def dp_memo(x, y, left_count, remain_k):
            if x > y:
                return 0
            ans = get_compressed_len(left_count + 1) + dp_memo(x + 1, y, 0, remain_k)
            if remain_k > 0:
                ans = min(ans, get_compressed_len(left_count) + dp_memo(x + 1, y, 0, remain_k - 1))
            for i in range(remain_k + 1):
                xx = x + i + 1
                if xx > y:
                    break
                if s[x] == s[xx]:
                    ans = min(ans, dp_memo(xx, y, left_count + 1, remain_k - i))
            return ans
        return dp_memo(0, len(s) - 1, 0, k)
