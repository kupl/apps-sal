class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        cost = 0
        left,right=0,0
        while right < len(s):
            cost += abs(ord(s[right])-ord(t[right]))
            if cost > maxCost:
                cost -= abs(ord(s[left])-ord(t[left]))
                left += 1
            else:
                ans = max(ans,right-left+1)
            right += 1
        return ans
            

