class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict
        cnt=defaultdict(int)
        for i in range(minSize-1,len(s)):
            low1=i-minSize+1
            low2=i-maxSize+1
            seen1=set()
            seen2=set()
            for k in range(low1,i+1):
                if s[k] not in seen1:
                    seen1.add(s[k])
            if low2>=0 and low1!=low2:
                for k in range(low2,i+1):
                    if s[k] not in seen2:
                        seen2.add(s[k])
                if len(seen2)<=maxLetters:
                    cnt[s[low2:i+1]]+=1
            if len(seen1)<=maxLetters:
                cnt[s[low1:i+1]]+=1
            
        if list(cnt.values()):
            return max(cnt.values())
        return 0

