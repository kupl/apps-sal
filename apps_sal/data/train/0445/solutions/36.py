class Solution:
    def minDifference(self, nums: List[int]) -> int:
        '''
        s1, s2, s3 = l1 - s4
        s1, s2, l1 = l2 - s3
        s1, l1, s2 = l2 - s3
        s1, l1, l2 = l3 - s2
        l1, s1, s2 = l2 - s3
        l1, s1, l2 = l3 - s2
        l1, l2, s1 = l3 - s2
        l1, l2, l3 = l4 - s1
        '''
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min([
            nums[-1] - nums[3],
            nums[-2] - nums[2],
            nums[-3] - nums[1],
            nums[-4] - nums[0]
        ])

