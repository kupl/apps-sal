class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        n = int((1 + math.sqrt(1+8*N))/2)
        print(n)
        ans = 0
        for i in range(1, n):
            if (2*N + i - i**2) != 0 and (2*N + i - i**2) % (2*i) == 0:
                ans += 1
        
        return ans
