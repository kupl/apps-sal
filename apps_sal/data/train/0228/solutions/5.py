class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel = 'aeiou'
        n = len(s)
        i = k
        window = s[:k]
        res = sum([1 for x in window if x in vowel])
        tmp = res
        
        while i <n:
            if s[i-k] in vowel:
                tmp -= 1
            if s[i] in vowel:
                tmp += 1
            res = max(res, tmp)
            i += 1
            
        return res
