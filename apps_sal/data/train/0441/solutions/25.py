class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        cnt = 0
        for c in range(1, floor(sqrt(2 * N)) + 1):
            if (2 * N) % c == 0:
                if ((2 * N / c) - c) % 2 == 1:
                    cnt += 1
                print(c)
        return cnt
