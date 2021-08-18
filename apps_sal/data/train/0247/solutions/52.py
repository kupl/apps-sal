class Solution:
    def getMinArr(self, arr, target, right=False):
        pre_sum = 0
        res = [float('inf') for i in range(len(arr))]
        sum_dict = {0: 0}
        if right:
            arr = arr[::-1]
        for i, num in enumerate(arr):
            pre_sum += num
            if i > 0:
                res[i] = res[i - 1]
            if pre_sum - target in sum_dict:
                cur_len = i - sum_dict[pre_sum - target] + 1
                res[i] = min(res[i], cur_len)
            sum_dict[pre_sum] = i + 1
        if right:
            res.reverse()
        return res

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left_min = self.getMinArr(arr, target)
        right_min = self.getMinArr(arr, target, True)

        min_len = float('inf')
        for i in range(len(arr) - 1):
            min_len = min(min_len, left_min[i] + right_min[i + 1])
        if min_len == float('inf'):
            return -1
        return min_len
