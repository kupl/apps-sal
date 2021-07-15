class Solution:
    def divs(self,x):
        memo = self.memo
        if x in memo:
            return memo[x]
        #
        res = 2 if x>1 else 1
        B   = {1,x}
        for a in range(2,x):
            if x<(a**2):
                break
            if not x%a:
                res += 1 if x==(a**2) else 2
                B.update( {a, x//a} )
            if res>4:
                break
            a += 1
        memo[x] = res,B
        return res,B
    def sumFourDivisors(self, A):
        self.memo = {}
        res = 0
        for x in A:
            r,B = self.divs(x)
            if r==4:
                res += sum(B)
        return res
