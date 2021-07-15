from math import inf
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def recurse(l,r):
            # if r<=l:
            #     return inf
            if self.dp.get((l,r),-1)!=-1:
                return self.dp[(l,r)]
            mnCut=inf
            flag=1
            for i in range(len(cuts)):
                if l<cuts[i]<r:
                    mnCut=min(mnCut,recurse(l,cuts[i])+recurse(cuts[i],r))
                    flag=0
            if flag==0:
                self.dp[(l,r)]=mnCut+r-l
            else:
                self.dp[(l,r)]=0
            return self.dp[(l,r)]
        self.dp={}
        cuts.sort()
        mn=recurse(0,n)
        # print(self.dp)
        return mn
