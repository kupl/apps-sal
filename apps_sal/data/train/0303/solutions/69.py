class Solution:
    def maxSumAfterPartitioning(self, l: List[int], k: int) -> int:
        def _max_sum(l, start, k, memo):
            if (len(l) - start) <= k:
                return (len(l) - start) * max(l[start:])

            if start in memo:
                return memo[start]

            max_sum = l[start]
            for i in range(1, k + 1):
                curr_sum = max(l[start:start + i]) * i + _max_sum(l, start + i, k, memo)
                max_sum = max(max_sum, curr_sum)

            memo[start] = max_sum
            return max_sum

        if not l:
            return 0

        return _max_sum(l, 0, k, dict())
