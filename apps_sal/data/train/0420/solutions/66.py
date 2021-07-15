class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res=0
        pos={0:-1}
        state=0  
        #记录子串中元音字母出现的次数，全为0说明都是偶数次
        #若有1，看看历史中有没有记录相同状态，中间子串就是全部偶数次
        vowels='aeiou'
        for i in range(len(s)):
            j=vowels.find(s[i])
            if j>=0:
                state^=1<<j
            if state in pos:
                res=max(res,i-pos[state])
            else:
                pos[state]=i
        return res
