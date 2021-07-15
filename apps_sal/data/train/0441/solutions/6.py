class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # res = 0
        # # explain math
        # upper_limit = ceil((2 * N + 0.25)**0.5 - 0.5)
        # for k in range(upper_limit):
        #     N -= k
        #     if N % k == 0:
        #         res += 1
        # return res
        res, k = 0, 1
       
        while (k*(k+1) <= 2*N):
            x = float(N)/k-(k+1)/2.0
            if ((2*N)%k == 0 and x.is_integer() ):
                res += 1
                #print(k,x)
            k+=1
        return res
