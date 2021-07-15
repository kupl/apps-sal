class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        mx = max(nums)

        low = 1
        high = mx
        best = mx

        while low < high:
            med = low + (high-low) // 2

            total = 0

            for num in nums:
                total += ceil(num / med)

            if total <= threshold:
                high = med
                best = min(best,med)
            else:
                low = med + 1


        return best

