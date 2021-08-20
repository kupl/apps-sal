class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        curr_sum = 0
        intervals = [(-200002, -100001), (-200002, -100001)]
        h = {0: -1}
        f = [[100001] * len(arr) for i in range(2)]
        for (index, a) in enumerate(arr):
            curr_sum += a
            f[1][index] = min(f[0][h[curr_sum - target]] + index - h[curr_sum - target] if curr_sum - target in h else 100001, f[1][index - 1])
            f[0][index] = min(f[0][index - 1] if index >= 1 else 100001, index - h[curr_sum - target] if curr_sum - target in h else 100001)
            h[curr_sum] = index
        return -1 if f[-1][-1] >= 100001 else f[-1][-1]
