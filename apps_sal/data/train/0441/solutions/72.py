class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if N == 1:
            return 1
        res = 1
        for i in range(2, int(N ** .5 + 1)):
            if N % i == 0:
                if i % 2 == 1:
                    res += 1
                j = (N // i)
                if i != j and j % 2 == 1:
                    res += 1
        if N % 2 == 1:
            res += 1

        return res
