import functools


class Solution:
    @functools.lru_cache(maxsize=None)
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @functools.lru_cache(maxsize=None)
        def dp(i: int, last: int, size: int, k: int) -> int:
            if k < 0:
                return float('inf')
            if i >= len(s):
                return 0
            answer: int = 0
            if ord(s[i]) - ord('a') == last:
                carry: int = 1 if size in (1, 9, 99) else 0
                answer = carry + dp(i + 1, last, size + 1, k)
            else:
                answer = min(1 + dp(i + 1, ord(s[i]) - ord('a'), 1, k), dp(i + 1, last, size, k - 1))
            return answer
        return dp(0, 26, 0, k)
