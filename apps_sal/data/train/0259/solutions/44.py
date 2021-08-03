class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''

        find m where    (num + m) // m    for all nums and sum to <= threshold

        '''

        i = 1
        j = max(nums)

        while i < j:
            m = (i + j) // 2

            total = 0
            for num in nums:
                total += (num + m - 1) // m  # ceil. division

            if total > threshold:
                i = m + 1
            elif total <= threshold:
                j = m

        return i
