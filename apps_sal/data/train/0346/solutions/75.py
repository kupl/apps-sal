class Solution:

    def checkOdd(self, num):
        if num % 2 == 0:
            return False
        return True

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIndices = []
        for i in range(len(nums)):
            if self.checkOdd(nums[i]):
                oddIndices.append(i)
        start = 0
        end = k - 1
        i = 0
        count = 0
        while end < len(oddIndices):
            if end == len(oddIndices) - 1:
                j = len(nums) - 1
            else:
                j = oddIndices[end + 1] - 1
            count = count + (oddIndices[start] - i + 1) * (j - oddIndices[end] + 1)
            i = oddIndices[start] + 1
            start = start + 1
            end = end + 1
        return count
