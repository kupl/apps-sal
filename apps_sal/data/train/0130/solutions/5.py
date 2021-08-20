class Solution:

    def numberOfArrays(self, s: str, k: int) -> int:
        import sys
        sys.setrecursionlimit(10 ** 9 + 7)

        @lru_cache(None)
        def ways(idx):
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0
            ans = 0
            num = 0
            for i in range(idx, len(s)):
                num = num * 10 + (ord(s[i]) - ord('0'))
                if num > k:
                    break
                ans = (ans + ways(i + 1)) % 1000000007
            return ans
        return ways(0)
