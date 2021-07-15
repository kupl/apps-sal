class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        #Look like start with some number, add up til sum = N
        #k + (k+1) + (k+2) + (k+i) = N
        #k*i + (0+1+2+..+i) = N
        #k*i + (i(i+1)/2) = N
        #k * i = (N - (i(i+1)/2)) -> full chunk % i == 0 -> k is start point
        
        i, ans = 1, 0
        while N > i * (i - 1) // 2:
            if (N - i * (i + 1) // 2) % i == 0:
                ans += 1
            i += 1
        return ans
