class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        (answer, k) = (0, 1)
        while N - k * (k - 1) // 2 > 0:
            if (N - k * (k - 1) // 2) % k == 0:
                answer += 1
            k += 1
        return answer
