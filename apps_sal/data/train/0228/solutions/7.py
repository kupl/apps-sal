class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        dic = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        for i in range(k):
            if s[i] in dic:
                ans += 1
        i = 0
        j = k
        temp = ans
        while j < len(s):
            if s[j] in dic:
                temp += 1
            if s[i] in dic:
                temp -= 1
            ans = max(ans, temp)
            i += 1
            j += 1
        return ans
