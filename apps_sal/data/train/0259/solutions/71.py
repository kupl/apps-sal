class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        low = 1
        high = 2 * max(nums)
        ans = float('inf')

        while low <= high:
            mid = (low + high) // 2
            m = sum(math.ceil(x / mid) for x in nums)
            if m <= threshold:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans
