class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        n = 0
        ans = 0
        while (N - n*(n+1)//2) > 0:
            if (N - n*(n+1)//2)%(n+1) == 0:
                ans +=1
            n +=1
        return ans

