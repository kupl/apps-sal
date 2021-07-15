class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        idx_dic = {0: -1}
        vowels = 'aeiou'
        state = ans = 0
        for i in range(len(s)):
            j = vowels.find(s[i])
            if j >= 0:
                state ^= 1 << j
            if state not in idx_dic:
                idx_dic[state] = i
            
            ans = max(ans, i - idx_dic[state])
        return ans
