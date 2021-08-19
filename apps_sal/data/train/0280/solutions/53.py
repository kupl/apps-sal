class Solution:

    def palindromePartition(self, s: str, k: int) -> int:

        @lru_cache(None)
        def dp(index, l):
            if l == 1:
                leftstr = s[index:]
                count = 0
                (left, right) = (0, len(leftstr) - 1)
                while left < right:
                    if leftstr[left] != leftstr[right]:
                        count += 1
                    left += 1
                    right -= 1
                return count
            if index == len(s) - 1:
                return 0
            minvalue = float('inf')
            for i in range(index + 1, len(s)):
                leftstr = s[index:i]
                count = 0
                (left, right) = (0, len(leftstr) - 1)
                while left < right:
                    if leftstr[left] != leftstr[right]:
                        count += 1
                    left += 1
                    right -= 1
                minvalue = min(minvalue, count + dp(i, l - 1))
            return minvalue
        return dp(0, k)
