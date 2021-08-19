class Solution:
    def minSumOfLengths(self, arr, target):
        inf = 2**31 - 1
        i, window, result = 0, 0, inf
        premin = [inf] * len(arr)

        # i: window start, j: window end
        for j, num in enumerate(arr):

            window += num
            while window > target:
                window -= arr[i]
                i += 1
            if window == target:
                # curr: length
             # print(premin, i, j)
                curr = j - i + 1
                if result > curr + premin[i - 1]:
                    result = curr + premin[i - 1]
                premin[j] = curr if curr < premin[j - 1] else premin[j - 1]

            else:
                premin[j] = premin[j - 1]

        return result if result < inf else -1
