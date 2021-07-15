class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = collections.defaultdict(int)
        
        for num in arr:
            cnt[num] += 1
            
        a = [(cnt[key], key) for key in cnt]
        a.sort(key = lambda x:x[0])
        
        ret = len(a)
        
        i = 0
        while k:
            if a[i][0] <= k:
                k -= a[i][0]
                ret -= 1
                
            else:
                break
                
            i += 1
            
        return ret
