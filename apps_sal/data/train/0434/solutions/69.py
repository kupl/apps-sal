class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        arr = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                arr.append(count)
                count = 0
        arr.append(count)
        if len(arr) == 1:
            return arr[0] - 1
        maxi = 0
        for j in range(1, len(arr)):
            maxi = max(maxi, arr[j - 1] + arr[j])
        return maxi
