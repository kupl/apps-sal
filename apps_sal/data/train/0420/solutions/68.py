class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        for window_size in range(len(s), -1, -1):
            end_pos = len(s) - window_size + 1
            for i in range(end_pos):
                substring = s[i:i + window_size]
                is_all_even = True
                for ch in 'aeiou':
                    if substring.count(ch) % 2:
                        is_all_even = False
                        break
                if is_all_even:
                    return window_size
        return 0
