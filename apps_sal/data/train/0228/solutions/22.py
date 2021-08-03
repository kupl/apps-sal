class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        i, j = 0, 0
        cnt = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        while j < n:
            if s[j] in vowels:
                cnt += 1
            if j == k - 1:
                break
            else:
                j += 1
        ans = max(ans, cnt)

        while j + 1 < n:
            if s[i] in vowels:
                cnt -= 1
            i += 1
            j += 1
            if s[j] in vowels:
                cnt += 1
            ans = max(ans, cnt)

        return ans
