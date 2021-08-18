class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:

        def summer(x):
            return x * (x - 1) / 2
        count = 0
        i = 1

        while summer(i) < N:
            if ((N - summer(i)) % i == 0):
                count += 1
            i += 1
        return count
