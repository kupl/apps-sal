class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        max_substring_size = 0
        s_len = len(s)
        for i in range(s_len):
            if max_substring_size > s_len - i:
                break
            vowel_counts = {'a':0,'e':0,'i':0,'o':0,'u':0}
            allEven = True
            for k, letter in enumerate(s[i:]):
                if letter in vowel_counts:
                    vowel_counts[letter] += 1
                    currently_all_even = True
                    for count in list(vowel_counts.values()):
                        if count % 2 == 1:
                            currently_all_even = False
                            break
                    allEven = currently_all_even
                if allEven and k + 1 > max_substring_size:
                    max_substring_size = k + 1
        return max_substring_size

