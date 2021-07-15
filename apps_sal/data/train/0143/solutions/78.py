class Solution:
    def totalFruit(self, ar: List[int]) -> int:
        l=list(set(ar))
        if len(l)<=2:
            return len(ar)
        else:
            m=0
            for i in range(0,len(ar)):
                l=[ar[i]]
                # c=0
                d=1
                for j in range(i+1,len(ar)):
                    if ar[j] in l:
                        l.append(ar[j])
                    elif ar[j] not in l and d==1:
                        d+=1
                        l.append(ar[j])
                    else:
                        break
                m=max(m,len(l))
            return m
                    
                    
                
               
        
        

