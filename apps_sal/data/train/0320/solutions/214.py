class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mul = [0 for i in range(len(nums))]
        inc = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            while nums[i]!=0:
                if nums[i]%2 == 1:
                    inc[i] += 1
                    nums[i] = nums[i]-1
                else:
                    mul[i] +=1
                    nums[i] //= 2
        return max(mul)+sum(inc)

