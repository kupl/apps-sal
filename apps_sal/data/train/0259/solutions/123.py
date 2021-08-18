class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        end = 1
        start = end

        def findSum(div):
            return sum([math.ceil(n / div) for n in nums])
        while True:
            if findSum(end) > threshold:
                start = end
                end *= 2
            else:
                break
        while end > start:
            mid = (start + end) // 2
            if findSum(mid) > threshold:
                start = mid + 1
            else:
                end = mid
        return end
