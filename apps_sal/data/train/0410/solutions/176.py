class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo={1:0}
        def getPower(x):
            if x in memo:
                return memo[x]
            if x%2==0:
                memo.update({x:getPower(x//2)+1})
                return memo[x]
            else:
                memo.update({x:getPower(x*3+1)+1})
                return memo[x]
        return sorted(map(lambda x: (getPower(x),x), range(lo,hi+1)))[k-1][1]
