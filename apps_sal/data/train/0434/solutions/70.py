class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        arr = [0]
        (count, flag) = (0, 0)
        for (idx, num) in enumerate(nums):
            if num == 0:
                if flag == 1:
                    arr.append(count)
                    count = 0
                arr.append(0)
                flag = 0
            elif num == 1:
                count += 1
                flag = 1
            if idx == len(nums) - 1:
                arr.append(count)
        arr.append(0)
        maxSum = 0
        for i in range(1, len(arr) - 1):
            if arr[i] == 0:
                maxSum = max(maxSum, arr[i - 1] + arr[i + 1])
        return maxSum
