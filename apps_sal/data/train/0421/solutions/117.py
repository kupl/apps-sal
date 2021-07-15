class Solution:
    def lastSubstring(self, s: str) -> str:
        max_char = 'a'
        curr_idx = []
        for i in range(len(s)):
            if s[i] > max_char:
                curr_idx = [i]
                max_char = s[i]
            elif s[i] == max_char:
                curr_idx.append(i)
        
        curr_max = ''
        for idx in curr_idx:
            if s[idx:] > curr_max:
                curr_max = s[idx:]
        
        return curr_max
