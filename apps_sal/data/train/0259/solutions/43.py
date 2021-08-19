class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """

        find m where    (num + m) // m    for all nums and sum to <= threshold

        """
        i = 1
        j = max(nums)
        m = (i + j) // 2
        ans = 0
        while i <= j:
            total = 0
            for num in nums:
                total += (num + m - 1) // m
            if total > threshold:
                i = m + 1
            elif total <= threshold:
                j = m - 1
                ans = m
            m = (i + j) // 2
        return ans
