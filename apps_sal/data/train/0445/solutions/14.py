class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        x = 0
        y = len(nums) - 1
        arr = []
        while x < y:
            arr.append(nums[x])
            arr.append(nums[y])
            x += 1
            y -= 1
        if x == y:
            arr.append(nums[x])
        arr.sort()
        self.ans = float('inf')
        self.min_diff(0, len(arr) - 1, arr, 3)
        return self.ans

    def min_diff(self, i, j, arr, depth):
        if depth == 0:
            self.ans = min(self.ans, arr[j] - arr[i])
            return
        self.min_diff(i + 1, j, arr, depth - 1)
        self.min_diff(i, j - 1, arr, depth - 1)
