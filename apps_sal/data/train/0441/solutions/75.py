class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        counter = 0
        n = 2
        cnum = []
        while n * (n + 1) / 2 <= N:
            conditionNo = int(N - n * (n + 1) / 2)
            if conditionNo % n == 0:
                counter = counter + 1
            n = n + 1
        return counter + 1
