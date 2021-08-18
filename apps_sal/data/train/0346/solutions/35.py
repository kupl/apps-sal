class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        noOfNiceSubArrays = 0
        even = 0
        oddList = []
        for i in range(n):
            if nums[i] % 2 == 0:
                even += 1
            else:
                oddList.append(even)
                even = 0
        oddList.append(even)
        for i in range(len(oddList) - k):
            noOfNiceSubArrays += (oddList[i] + 1) * (oddList[i + k] + 1)

        return noOfNiceSubArrays
