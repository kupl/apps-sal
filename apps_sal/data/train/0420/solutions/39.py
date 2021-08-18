class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        for window_size in range(len(s), -1, -1):
            check_range = len(s) - window_size + 1
            for i in range(check_range):
                check_wr = s[i: i + window_size]
                right_string = True
                for ch in 'aeiou':
                    if check_wr.count(ch) % 2:
                        right_string = False
                        break
                if right_string:
                    return window_size
        return 0
