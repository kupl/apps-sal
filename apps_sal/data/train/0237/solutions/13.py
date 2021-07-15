class Solution:
    
    def f(self, A):
        ret = 0
        
        cnt = 0
        for a in A:
            if not cnt:
                if not a:
                    cnt += 1
            else:
                if not a:
                    cnt += 1
                else:
                    ret += (cnt*(cnt+1)) // 2
                    cnt = 0

        if cnt: ret += (cnt*(cnt+1)) // 2
                    
        return ret
        pass

    def numSubarraysWithSum(self, A: List[int], k: int) -> int:
        ret = 0
                
        if not k: return self.f(A)
        
        mp = { 0 : 1 }
        cnt = 0

        for a in A:
            cnt += a
            
            if cnt not in mp:
                mp[cnt] = 0
            mp[cnt] += 1
            
            if cnt - k in mp:
                ret += mp[cnt - k]
            
        return ret
