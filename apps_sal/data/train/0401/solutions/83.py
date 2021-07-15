
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums = sorted(nums)
        s = sum(nums)
        if s % 3 == 0:
            return s
        one = [x for x in nums if x%3 == 1]
        two = [x for x in nums if x%3 == 2]
        three = [x for x in nums if x%3 == 0]
        if s % 3 == 1:
            if one and len(two)>1:
                return s - min(one[0], sum(two[0:2]))
            if one:
                return s - one[0]
            return s - sum(two[0:2])
        if s % 3 == 2:
            if len(one)>1 and two:
                return s - min(sum(one[0:2]), two[0])
            if len(one)>1:
                return s - sum(one[0:2])
            return s - two[0]
