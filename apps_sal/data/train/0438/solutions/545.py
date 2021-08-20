class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        from bisect import bisect_left
        zeros = [0, len(arr) + 1]
        ans = -1
        for i in reversed(list(range(len(arr)))):
            index = bisect_left(zeros, arr[i])
            zeros.insert(index, arr[i])
            if m in (zeros[index + 1] - arr[i] - 1, arr[i] - zeros[index - 1] - 1):
                return i
        return -1
