class Solution:
    def minSumOfLengths(self, arr, target):
        result = inf = 2**31 - 1
        i = window = count = 0
        # preMin: store previous shortest length
        preMin = [(-1, inf)]

        # i: window start, j: window end
        for j, num in enumerate(arr):
            window += num
            while window > target:
                window -= arr[i]
                i += 1
            if window == target:
                # curr: current length
                curr = j - i + 1
                n = 0
                # find first minimal length before window start i
                for index, length in preMin[::-1]:
                    if index <= i - 1:
                        n = length
                        break
                # update result if less
                if result > curr + n:
                    result = curr + n
                # update shortest length if less
                if curr < preMin[-1][-1]:
                    preMin.append((j, curr))
                # early stopping if found two single targets
                if curr == 1:
                    count += 1
                if count == 2:
                    return 2

        return result if result < inf else -1
