class Solution:
    def reorderedPowerOf2(self, N: int) -> bool: 
        if N==1:
            return True
        elif N==2:
            return True
       
        
        max_v = int(''.join((sorted(list(str(N)), reverse=True))))
        canidates = 2
        while True:
            print (canidates)            
            if len(str(canidates))==len(str(N)):
                canidates_memo = collections.Counter(str(canidates))
                N_memo = collections.Counter(str(N))
                success = True
                for k in canidates_memo:
                    if k not in N_memo or canidates_memo[k]!=N_memo[k]:
                        success=False
                        break
                if success:
                    return True
            if canidates<max_v:
                canidates *=2
            else:
                break
        return False
        

