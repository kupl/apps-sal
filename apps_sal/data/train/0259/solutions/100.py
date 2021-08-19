import math


class Solution:

    def smallestDivisor(self, nums: List[int], t: int) -> int:

        def mine2(n, nums):
            nums_copy = nums[:]
            nums_copy = list([math.ceil(x / n) for x in nums_copy])
            return sum(nums_copy)

        def mine(left, right, nums, t, l):
            if right > left:
                mid = (left + right) // 2
                if mine2(mid, nums) <= t:
                    right = mid - 1
                    l.append(mid)
                else:
                    left = mid + 1
                return mine(left, right, nums, t, l)
            else:
                if left > 0:
                    if mine2(left, nums) <= t:
                        l.append(left)
                if right > 0:
                    if mine2(right, nums) <= t:
                        l.append(right)
                return l
        l = []
        return min(mine(1, max(nums), nums, t, l))
