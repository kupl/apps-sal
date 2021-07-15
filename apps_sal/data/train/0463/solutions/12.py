class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        # 三种情况，从头到中间某个地方进行reverse；
        # 从中间到最后进行reverse，中间的某一段进行reverse
        total, res, min2, max2 = 0, 0, float('inf'), float('-inf')
        for a, b in zip(nums[:-1], nums[1:]):
            total += abs(a - b)
            res = max(res, abs(nums[0] - b) - abs(a - b))
            res = max(res, abs(nums[-1] - a) - abs(a - b))
            min2, max2 = min(min2, max(a, b)), max(max2, min(a, b))
        return total + max(res, (max2 - min2) * 2)
