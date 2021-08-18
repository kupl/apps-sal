class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        n, j = len(nums), sum(nums)
        i = (j + n) // threshold
        i = 1 if i == 0 else i
        while i < j - 1:
            k = (i + j) // 2
            ss = sum([math.ceil(n / k) for n in nums])
            if ss > threshold:
                i = k
            else:
                j = k

        if sum([math.ceil(n / i) for n in nums]) <= threshold:
            return i
        else:
            return j
