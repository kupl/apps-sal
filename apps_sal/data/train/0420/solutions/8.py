import collections


class Solution:

    def findTheLongestSubstring(self, s: str) -> int:

        for substr_len in range(len(s), -1, -1):
            end_remove = len(s) - substr_len + 1

            for start in range(end_remove):
                even = True
                sub_str = s[start:start + substr_len]

                for vowel in 'aeiou':
                    if sub_str.count(vowel) % 2 != 0:
                        even = False
                        break
                if even == True:
                    return substr_len
