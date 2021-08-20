class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        (ans, count, seen) = (0, 0, {})
        for (i, hour) in enumerate(hours):
            count = count + 1 if hour > 8 else count - 1
            if count > 0:
                ans = i + 1
            else:
                if count not in seen:
                    seen[count] = i
                if count - 1 in seen:
                    ans = max(ans, i - seen[count - 1])
        return ans
