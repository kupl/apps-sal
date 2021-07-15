from collections import defaultdict
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        n = len(nums)
        elemfreq = defaultdict(int)
        freqcnt = defaultdict(int)
        
        i = 0
        n_distinct = 0
        maxfreq = 0
        
        maxprefix = None
        
        
        
        while i != n:
            x = nums[i]
            
            if elemfreq[x] == 0:
                n_distinct += 1
                elemfreq[x] += 1
                freqcnt[1] += 1
            else:
                freqcnt[elemfreq[x]] -= 1
                freqcnt[elemfreq[x]+1] += 1
                elemfreq[x] += 1
            
            maxfreq = max(maxfreq, elemfreq[x])
            
            if maxfreq == 1:
                maxprefix = i
            elif (freqcnt[1] == 1) and (freqcnt[maxfreq] == n_distinct-1):
                maxprefix = i
            elif (freqcnt[maxfreq] == 1) and (freqcnt[maxfreq-1] == n_distinct-1):
                maxprefix = i
            
            i += 1
            
        return maxprefix+1
