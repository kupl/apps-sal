class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        ans = {}
        
        for i in range(lo,hi+1):
            j = i
            s=0
            while(i != 1):
                if(i % 2 == 0):
                    i = i // 2
                else:
                    i = i * 3 + 1
                s =s+1
                
            ans[j] = s
        
        ans = sorted(list(ans.items()), key=lambda x: x[1])
        
        return(ans[k-1][0])
        
        
            
            

