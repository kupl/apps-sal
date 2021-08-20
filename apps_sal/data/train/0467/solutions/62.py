class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            (curSum, curAns) = (1 + nums[i], 2)
            for j in range(2, int(sqrt(nums[i])) + 1):
                if nums[i] % j == 0:
                    if j == nums[i] // j:
                        curSum += nums[i] // j
                        curAns += 1
                    else:
                        curSum += j + nums[i] // j
                        curAns += 2
            if curAns == 4:
                res += curSum
        return res
