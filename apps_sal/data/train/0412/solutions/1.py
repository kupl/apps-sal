class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > d * f:
            return 0
        total_sum = 0
        cache_sum = []
        if target > d * (1 + f) / 2:
            target = d * (1 + f) - target
        for i in range(target, -1, -1):
            num = 0 if i > f else 1
            total_sum += num
            cache_sum.append(total_sum)
        cache_sum = cache_sum[::-1]
        cache_sum[0] = cache_sum[1]
        for i in range(2, d + 1):
            total_sum = 0
            for j in range(target, -1, -1):
                total_sum += cache_sum[max(j - f, 0)] - cache_sum[j]
                cache_sum[j] = total_sum
        return cache_sum[-1] % (10 ** 9 + 7)
