class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        self.vowels = ['a', 'e', 'i', 'o', 'u']

        def isVowel(char):
            return char in self.vowels
        i = 0
        j = 0
        cur_count = 0
        result = 0
        length = len(s)
        while i < length and j < length:
            if isVowel(s[j]):
                cur_count += 1
            if j - i + 1 >= k:
                result = max(result, cur_count)
                if isVowel(s[i]):
                    cur_count -= 1
                i += 1
            j += 1
        return result
