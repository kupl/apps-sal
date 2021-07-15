class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        def vowel_letters(ch):
            if ch in ['a','e','i','o','u']:
                return True
            return False

        temp = [1 if vowel_letters(i) else 0 for i in s]

        su = sum(temp[:k])
        m = su

        for i in range(k,len(temp)):
            su += temp[i]-temp[i-k]
            m = max([su,m])

        return m
