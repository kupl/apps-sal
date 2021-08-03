class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        s = sum(nums)
        l = len(nums)
        L = max((s + threshold - 1) // threshold, 1) - 1
        # worst case: every num is just one more of multiple of answer
        t_ = max(threshold - l, 1)
        U = (s + t_ - 1) // t_
        while L + 1 < U:
            m = (L + U) // 2
            if sum((x + m - 1) // m for x in nums) <= threshold:
                U = m
            else:
                L = m
        return U
