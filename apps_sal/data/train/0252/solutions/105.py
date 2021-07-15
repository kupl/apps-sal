class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals=[]
        for i,r in enumerate(ranges):
            intervals.append([i-r,i+r])
        intervals.sort(key=lambda x:[x[0],-x[1]])
        #print(intervals)
        count=0
        def getnext(l):
            rel=[]
            for i in intervals:
                if l>=i[0] and l<i[1]:
                    rel.append(i)
            rel.sort(key=lambda x:x[1],reverse=True)
            return rel[0] if rel else None
        
        j=0
        while j<n:
            iv=getnext(j)
            #print(count,j,iv)
            if iv:
                j=iv[1]
                count+=1
            else:
                return -1
        return count
