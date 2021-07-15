class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        i = 1
        num_sums = 0
        while (N//i - i//2 +(i%2==0)> 0):
            first = N//i - i//2
            if (i%2 == 0):
                first += 1
            last = N//i + i//2

            s = (first + last)*i//2
            
            if (s == N):
                num_sums += 1
            
            # print(\"{} - {} = {}\".format(first, last, s))
            i += 1
        return num_sums
