class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_valid(select_num: int):
            res = sum([math.ceil(num / select_num) for num in nums])
            return None if res > threshold else res

        if not nums:
            return 0
        left, right = 1, 1000000000
        while left < right:
            middle = (left + right) // 2
            if is_valid(middle):
                right = middle
            else:
                left = middle + 1

        return left if is_valid(left) else right
