class Solution:
    def lenLongestFibSubseq(self, a: List[int]) -> int:
        s=set(a)
        c=0
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                x,y,l=a[i],a[j],2
                while x+y in s:
                    x,y=y,x+y
                    l+=1
                c=max(c,l)
        return c if c>2 else 0

