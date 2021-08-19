class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        init = len([x for x in s[:k] if x in vowels])
        ans = init
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                init -= 1
            if s[i + k - 1] in vowels:
                init += 1
            ans = max(ans, init)
        return ans
