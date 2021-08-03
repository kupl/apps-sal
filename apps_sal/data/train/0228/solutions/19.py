class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        m, beg, end = len(s), 0, 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        maxi, count = 0, 0

        while end < m:

            if s[end] in vowels:
                count += 1

            if end - beg + 1 >= k:
                maxi = max(maxi, count)
                if s[beg] in vowels:
                    count -= 1
                beg += 1

            end += 1

        return maxi
