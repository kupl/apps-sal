class Solution:
    def findTheLongestSubstring(self, S: str) -> int:
        vowels='aeiou'
        seen={0:-1}
        ans=cur=0
        for i,c in enumerate(S):
            if c in vowels:
                cur^=1<<(ord(c)-97)
            if cur not in seen:
                seen[cur]=i
            else:
                ans=max(ans,i-seen[cur])
        return ans
