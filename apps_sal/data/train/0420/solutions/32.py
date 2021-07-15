class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        remainder_pos_dict = dict()
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = {ch: 0 for ch in vowels}
        max_length = 0
        
        for pos, ch in enumerate(s):
            if ch in vowels:
                vowel_count[ch] += 1
            remainders = (vowel_count['a'] % 2, vowel_count['e'] % 2, vowel_count['i'] % 2, vowel_count['o'] % 2, vowel_count['u'] % 2)
            if all(map(lambda x: x == 0, remainders)):
                max_length = max(max_length, pos + 1)
                continue
            if remainders not in remainder_pos_dict:
                remainder_pos_dict[remainders] = pos
                continue
            prefix_tail = remainder_pos_dict[remainders]
            length = pos - prefix_tail
            max_length = max(length, max_length)
        
        return max_length
