def parent(p,i):
    if p[i]!=i:
        p[i]=parent(p,p[i])
    return p[i]


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        p=[0]*len(light)
        c=[0]*len(p)
        for i in range(len(p)):
            p[i]=i
        x=0
        ans=0
        for j in light:
            i=j-1
            x+=1
            c[i]=1
            if i-1>-1 and c[i-1]!=0:
                p[i]=parent(p,i-1)
                c[p[i]]+=1
            if i+1<len(light) and c[i+1]!=0:
                c[p[i]]+=c[i+1]
                p[i+1]=p[i]
            if c[p[i]]==x and c[0]!=0:
                #print(c)
                #print(p)
                #print()
                ans+=1
        return ans
