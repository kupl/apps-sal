class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        max_res = [0] * len(arr)
        max_start = [0] * len(arr)
        max_end = [0] * len(arr)
        for (i, n) in enumerate(arr):
            max_end[i] = n if i == 0 else max(n, max_end[i - 1] + n)
        print(max_end)
        for (i, n) in list(enumerate(arr))[::-1]:
            max_start[i] = n if i == len(arr) - 1 else max(n, max_start[i + 1] + n)
        print(max_start)
        for (i, n) in enumerate(arr):
            max_left = n if i == 0 else max_end[i - 1]
            max_right = n if i == len(arr) - 1 else max_start[i + 1]
            max_res[i] = max(max_left, max_right, max_left + max_right)
        print(max_res)
        return max(max_res)
