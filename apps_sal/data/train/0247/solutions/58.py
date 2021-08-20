class Solution:

    def minSumOfLengths(self, arr, target):
        result = inf = 2 ** 31 - 1
        i = window = 0
        premin = [inf] * len(arr)
        for (j, num) in enumerate(arr):
            window += num
            while window > target:
                window -= arr[i]
                i += 1
            if window == target:
                curr = j - i + 1
                if result > curr + premin[i - 1]:
                    result = curr + premin[i - 1]
                premin[j] = curr if curr < premin[j - 1] else premin[j - 1]
            else:
                premin[j] = premin[j - 1]
        return result if result < inf else -1
