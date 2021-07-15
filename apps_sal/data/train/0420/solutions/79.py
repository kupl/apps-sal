class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        vowels = set('aeiou')
        
        odd = {'' : -1}
        key = ''
        res = 0
        
        window = collections.Counter()
        vowel_count = [window]
        for i,char in enumerate(s):
            if char in vowels:
                window[char] += 1
                key = ''.join(c for c in window if window[c]&1)
                if key in odd:
                    res = max(i - odd[key], res)
                else:
                    odd[key] = i
            else:
                res = max(i - odd[key], res)
        else:
            res = max(i - odd[key], res)

        return res
