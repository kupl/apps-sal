class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        arr = []
        for i in range(len(nums)):
            if nums[i] == 1:
                arr.append(i)
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] - 1 < k:
                return False
        return True
