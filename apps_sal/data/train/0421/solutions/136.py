class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s: return None
        first = {}
        for i, letter in enumerate(s):
            if letter not in first: first[letter] = [i]
            else: first[letter].append(i)
        first_letter = max(first.keys())
        res = first_letter
        for idx in first[first_letter]:
            res = max(res, s[idx:])
        return res
            
        

