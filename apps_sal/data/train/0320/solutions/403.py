class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def makeeven():
            did = 0
            for i in range(len(nums)):
                if nums[i] & 1:
                    nums[i] -= 1
                    did += 1
            return did

        def halv():
            did = False
            for i in range(len(nums)):
                if nums[i]:
                    nums[i] >>= 1
                    did = True
            return did
        count = 0
        while any(nums):
            count += (makeeven())
            count += int(halv())
        return count
