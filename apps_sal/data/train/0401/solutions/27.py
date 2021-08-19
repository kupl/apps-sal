class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        nums.sort()
        rest = total % 3
        if not rest:
            return total
        (a, b) = (0, 0)
        for n in nums:
            if b and n > b:
                break
            mod = n % 3
            if mod:
                if rest == mod:
                    return total - n
                elif not a:
                    a = n
                elif not b:
                    b = a + n
        return total - b
