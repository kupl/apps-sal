class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pre_index, curr_sum = 0, 0
        f = [100001] * (len(arr) + 1)
        ans = 100001
        for index, a in enumerate(arr):
            curr_sum += a
            while curr_sum > target:
                curr_sum -= arr[pre_index]
                pre_index += 1
            if curr_sum == target:
                ans = min(f[pre_index] + index + 1 - pre_index, ans)
                f[index + 1] = min(f[index], index + 1 - pre_index)
            else:
                f[index + 1] = f[index]
        return -1 if ans >= 100001 else ans
