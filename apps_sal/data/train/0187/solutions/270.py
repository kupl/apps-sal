class Solution:
    def minOperationsMaxProfit(self, c: List[int], b: int, r: int) -> int:
        ans=[0]
        i=0
        while i<len(c):
            if c[i]<=4:
                ans.append(ans[-1]+c[i]*b-r)
            elif i+1<len(c):
                c[i+1]+=c[i]-4
                ans.append(ans[-1]+4*b-r)
            else:
                c.append(c[i]-4)
                ans.append(ans[-1]+4*b-r)
            i+=1
        m=max(ans)
        return -1 if m==0 else ans.index(m)
