class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        curr=0
        maxcurr=0
        c=r=o=a=k=0
        for i in croakOfFrogs:
            if i=='c':
                c+=1
                curr+=1
            elif i=='r':
                r+=1
            elif i=='o':
                o+=1
            elif i=='a':
                a+=1
            else:
                k+=1
                curr-=1
            maxcurr=max(curr,maxcurr)
            if c<r or r<o or o<a or a<k:
                return -1
        if curr==0 and c==r and r==o and o==a and a==k:
            return maxcurr
        return -1
