class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        lengths = [len(arr) + 1]*(len(arr) + 1)
        i = 0
        j = 0
        s = 0
        min_two_sum = len(arr) + 1
        while j <= len(arr):
            if s < target:
                if j == len(arr):
                    break
                if j > 0:
                    lengths[j] = lengths[j - 1]
                s += arr[j]
                j += 1
            elif s > target:
                s -= arr[i]
                i += 1
            else:
                lengths[j] = min(lengths[j - 1], j - i)
                min_two_sum = min(min_two_sum, lengths[i] + j - i)
                if j == len(arr):
                    break
                s += arr[j]
                j += 1
        if min_two_sum > len(arr):
            min_two_sum = -1
        return min_two_sum

