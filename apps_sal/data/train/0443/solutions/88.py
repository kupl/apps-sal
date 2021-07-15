class Solution:
    def numTeams(self, r: List[int]) -> int:
        s=0
        for i in range(len(r)):
            a=0
            b=0
            c=0
            d=0
            for j in range(0,i):
                if r[j]<r[i]:
                    a+=1
                else:
                    b+=1
            for j in range(i+1,len(r)):
                if r[j]>r[i]:
                    c+=1
                else:
                    d+=1
            s+=a*c+b*d
        return s

