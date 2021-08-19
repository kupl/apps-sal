class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # 2N = 2xk + k(k + 1) => 2N = k(2x + k + 1) => x = N/k - (k + 1)/2 => 2N >= k(k + 1)
        # => 2N + 1/2 >= (k + 1/4)^2 => k <= sqrt(2N + 1/4) - 1/2
        count = 0
        limit = ceil(sqrt(2 * N + 0.25) - 0.5)
        for k in range(1, limit + 1):
            if (N - k * (k + 1) // 2) % k == 0:
                count += 1
        return count
