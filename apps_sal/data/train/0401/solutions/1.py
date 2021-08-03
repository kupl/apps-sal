class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        if sum(nums) % 3 == 0:
            return sum(nums)

        mod1 = [num for num in nums if num % 3 == 1]
        mod2 = [num for num in nums if num % 3 == 2]
        mod1_min = min(mod1 or [float('inf')])
        mod2_min = min(mod2 or [float('inf')])

        if mod1_min != float('inf'):
            mod1.remove(mod1_min)

        if mod2_min != float('inf'):
            mod2.remove(mod2_min)

        possibilities = [
            sum(nums) - mod1_min,
            sum(nums) - mod2_min,
            sum(nums) - mod1_min - min(mod1 or [float('inf')]),
            sum(nums) - mod2_min - min(mod2 or [float('inf')]),
        ]

        return max([
            pos for pos in possibilities if pos % 3 == 0
        ] or [0])
