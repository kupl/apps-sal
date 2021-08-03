class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_substring = 0
        curr_substring = 0

        left = right = diff = 0

        while right < len(s):
            local_diff = abs(ord(s[right]) - ord(t[right]))
            if diff + local_diff <= maxCost:
                diff += local_diff
                right += 1
                curr_substring += 1
                max_substring = max(curr_substring, max_substring)
            else:
                if left == right:
                    right += 1
                else:
                    diff -= abs(ord(s[left]) - ord(t[left]))
                    curr_substring -= 1
                left += 1

        return max_substring
