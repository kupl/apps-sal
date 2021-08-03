class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        l = 1
        r = 2**31 - 1
        def calc(cand): return sum(ceil(x / cand) for x in nums)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if calc(mid) > threshold:
                l = mid
            else:
                r = mid
        if calc(l) <= threshold:
            return l
        else:
            return r
