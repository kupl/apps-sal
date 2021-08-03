class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = 0
        l = len(nums)
        while True:

            allZeros = True

            for i in range(l):

                if nums[i] != 0:
                    allZeros = False
                if nums[i] % 2:
                    count += 1
                    nums[i] -= 1

            if allZeros:
                return count
            flag = False
            for i in range(l):
                if nums[i] != 0:
                    flag = True
                    nums[i] = nums[i] // 2
            if flag:
                count += 1
