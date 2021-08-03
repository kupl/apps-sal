class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # Bounded sliding window solution

        vowel = set('aeiou')
        leftwindow = 0

        ans = 0
        temp = 0

        for rightwindow in range(len(s)):

            # expand the window
            if rightwindow < k:
                if s[rightwindow] in vowel:
                    temp += 1
                    ans = max(temp, ans)
                continue

            leftChar = s[leftwindow]
            rightChar = s[rightwindow]

            if rightChar in vowel and leftChar in vowel:
                pass

            elif rightChar in vowel:
                temp += 1

            elif leftChar in vowel:
                temp -= 1

            ans = max(temp, ans)
            leftwindow += 1

        return ans
