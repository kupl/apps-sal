class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        curr_sum = 0 
        h = {0 : 0}
        f = [100001] * (len(arr) + 1)
        ans = 100001
        for index, a in enumerate(arr):
            curr_sum += a
            if curr_sum - target in h:
                ans = min(f[h[curr_sum - target]] + index + 1 - h[curr_sum - target], ans)
                f[index + 1] = min(f[index], index + 1 - h[curr_sum - target]) 
            else:
                f[index + 1] = f[index]
            h[curr_sum] = index + 1
        return -1 if ans >= 100001 else ans
