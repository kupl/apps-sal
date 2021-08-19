class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        k = 1
        count = 0
        while N / k - k / 2 > 0:
            print(k)
            if k % 2 != 0 and N % k == 0:
                count += 1
            elif N / k == N // k + 0.5:
                count += 1
            k += 1
        return count
