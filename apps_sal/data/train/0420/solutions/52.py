class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dic = {0: -1}
        res = state = 0
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        for i, c in enumerate(s):
            if c in vowels:
                state ^= vowels[c]
            if state not in dic:
                dic[state] = i
            else:
                res = max(res, i-dic[state])
                
        return res
