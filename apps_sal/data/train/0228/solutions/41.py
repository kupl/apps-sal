class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set({'a','e','i','o','u'})
        curr = 0
        maxx = 0
        for i in range(k):
            if s[i] in vowel:
                curr+=1
                maxx+=1
        for i in range(1, len(s)-k+1):
            if s[i+k-1] in vowel:
                curr +=1
            if s[i-1] in vowel:
                curr -=1
            if curr == k:
                return curr
            if curr >= maxx:
                maxx = curr
        return maxx
            

