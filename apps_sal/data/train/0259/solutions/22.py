class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)

        while lo < hi:
            mid = (lo+hi)//2                        
            print(sum([math.ceil(n/mid) for n in nums]))
            if sum([math.ceil(n/mid) for n in nums]) <= threshold:
                hi = mid
            else:
                lo = mid+1

        return lo
