class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = i = ans = 0
        for j in range(len(s)):
            c = s[j]
            cnt += (s[j] in 'aeiou')
            if j >= k:
                cnt -= (s[i] in 'aeiou')
                i += 1
            
            if j >= k - 1:
                ans = max(ans, cnt)
        return ans
