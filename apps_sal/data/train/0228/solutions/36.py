class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vowel = 0
        max_vowel = 0
        front = 0
        for i in range(len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or (s[i] == 'o') or (s[i] == 'u'):
                vowel += 1
                print(s[i])
            if i >= k - 1:
                max_vowel = max(max_vowel, vowel)
                front = s[i - k + 1]
                if front == 'a' or front == 'e' or front == 'i' or (front == 'o') or (front == 'u'):
                    vowel -= 1
        return max_vowel
