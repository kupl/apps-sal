class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        num_solutions = 0
        for i in range(1, ceil(sqrt(2 * N))):
            if(N - (i * (i - 1)) / 2) / i > 0 and (N - (i * (i - 1)) / 2) / i == floor((N - (i * (i - 1)) / 2) / i):
                print(i)
                num_solutions += 1

        return num_solutions
