class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        
        cnt = Counter(s)
        
        for x in t:
            if x in cnt.keys() and cnt[x] > 0:
                cnt[x] -= 1
        
        ans = 0
        # print(cnt)
        for x in cnt.values():
            ans += abs(x)
        
        return ans
