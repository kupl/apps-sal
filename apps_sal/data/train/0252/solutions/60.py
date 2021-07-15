class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        l=[]
        for i in range(n+1):
            l.append((i-ranges[i], i+ranges[i]))
        l.sort()
        maxlen=0
        curpos=0
        res=0
        while maxlen<n:
            new=maxlen
            while curpos<=n and l[curpos][0]<=maxlen:
                if l[curpos][1]>maxlen:
                    new=max(new, l[curpos][1])
                curpos+=1  
            if maxlen==new:
                return -1
            res+=1
            maxlen=new
        return res     

