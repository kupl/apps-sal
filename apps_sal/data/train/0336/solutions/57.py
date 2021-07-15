class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1 = {}
        count2 = {}
        
        for ch in s:
            if ch not in count1:
                count1[ch] = 0
            count1[ch]+=1
                
        for ch in t:
            if ch not in count2:
                count2[ch] = 0
            count2[ch]+=1        
        
        count = 0
        for ch in count2:
            if ch in count1:
                if count1[ch]==count2[ch]:
                    continue
                else:
                    # We have the case where count is greater
                    if count2[ch]>count1[ch]:
                        diff = count2[ch]-count1[ch]
                        count+=diff
                        continue
                    # We have the case where count is lesser
                    else:
                        pass
            else:
                count+=count2[ch]
        return count
