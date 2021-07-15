import math
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 1
        maxK = int(math.sqrt(N)) * 2
        for k in range(2, maxK+1):
            if (k*(k - 1 )/2) >= N:
                continue
            if (N - (k*(k - 1 )/2)) % k == 0:
                print(k)
                res += 1
        

        return res
