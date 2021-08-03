class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # high = math.ceil(max(nums) * len(nums) / threshold)
        # low = math.ceil(sum(nums) / threshold)
        low, high = math.ceil(sum(nums) / threshold), math.ceil(sum(nums) / (threshold - len(nums)))

        def binary_search(low, high):
            if high > low:
                mid = (high + low) // 2
                tot = 0
                for num in nums:
                    tot += math.ceil(num / mid)
                if tot <= threshold:
                    return binary_search(low, mid)
                else:
                    return binary_search(mid + 1, high)
            else:
                return high
        return binary_search(low, high)
