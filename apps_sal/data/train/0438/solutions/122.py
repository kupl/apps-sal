class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        seen = dict()
        
        ans = -1
        ct = 0
        latestGood = dict()
        for pos in arr:
            ct+=1
            mi, ma = pos, pos
            
            if pos-1 in seen:
                mi = min(seen[pos-1][0], mi)
            
            if pos+1 in seen:
                ma = max(seen[pos+1][1], ma)                                    
            
            seen[pos] = (mi, ma)
            
            if pos-1 in seen:
                seen[pos-1] = (mi, ma)
            
            if pos+1 in seen:
                seen[pos+1] = (mi, ma)
                
            if mi in seen:
                seen[mi] = (mi, ma)
            
            if ma in seen:
                seen[ma] = (mi, ma)
            
            if ma-mi+1==m:
                ans=ct
                
                latestGood[mi] = ma
                latestGood[ma] = mi
            else:                                
                if pos-1 in latestGood:
                    if latestGood[pos-1] in latestGood:
                        latestGood.pop(latestGood[pos-1])
                        
                    if pos-1 in latestGood:
                        latestGood.pop(pos-1)
                    
                if pos+1 in latestGood:
                    if latestGood[pos+1] in latestGood:
                        latestGood.pop(latestGood[pos+1])
                    
                    if pos+1 in latestGood:
                        latestGood.pop(pos+1)
                
                if len(latestGood)>0:
                    ans=ct
            
                
        return ans

