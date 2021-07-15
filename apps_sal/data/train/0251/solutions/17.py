class Solution:
    def clumsy(self, N: int) -> int:
        x = ['*', '//', '+', '-'] * (10000//4)
        x = iter(x)
        ans = str(N)
        i = N-1
        while i > 0:
            op = next(x)
            ans += (op+str(i))
            i -= 1
        return eval(ans)
            


