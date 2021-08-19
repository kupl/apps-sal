class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        return self.dfs_helper(arr, n, 1, n, m)

    def dfs_helper(self, arr, step, left, right, target):
        if left > right or right - left + 1 < target:
            return -1
        if right - left + 1 == target:
            return step
        breakpoint = arr[step - 1]
        if left <= breakpoint <= right:
            res = max(self.dfs_helper(arr, step - 1, left, breakpoint - 1, target), self.dfs_helper(arr, step - 1, breakpoint + 1, right, target))
        else:
            res = self.dfs_helper(arr, step - 1, left, right, target)
        return res
