class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_len = 1
        maxi = nums[0]
        mini = nums[0]
        start = 0
        temp = nums[start:start+1]
        for i in range(1, len(nums)):
            temp.append(nums[i])
            if nums[i] > maxi:
                maxi = nums[i]
            if nums[i] < mini:
                mini = nums[i]
            if maxi - mini <= limit:
                max_len = max(max_len, len(temp))
            else:
                temp.pop(start)
                maxi = max(temp)
                mini = min(temp)
        return max_len

