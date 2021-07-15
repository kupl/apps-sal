class Solution:
    def maxRepOpt1(self, text: str) -> int:
        d={}
        f={}
        for i in text:
            d[i]=[]
            f[i]=f.get(i,0)+1
        for i in list(d.keys()):
            s=0
            same=0
            diff=0
            for j in text:
                if j==i:
                    s=1
                if j==i and s==1:
                    if diff:
                        d[i].append(-diff)
                    same+=1
                    diff=0
                else:
                    if same:
                        d[i].append(same)
                    diff+=1
                    same=0
            if same:
                d[i].append(same)
            if diff:
                d[i].append(-diff)
        l=0
        print(d)
        for i in list(d.keys()):
            for j,v in enumerate(d[i]):
                if v>0:
                    l=max(l,v)
                    if j+2<len(d[i]) and d[i][j+1]==-1  :
                        if d[i][j+2]+d[i][j]<f[i]:
                            l=max(l,d[i][j+2]+d[i][j]+1)
                        else:
                            l=max(l,d[i][j+2]+d[i][j])
                            
                    else:
                        if d[i][j]<f[i]:
                            l=max(l,d[i][j]+1)
        return l
                        
                    
                    
                 
            

