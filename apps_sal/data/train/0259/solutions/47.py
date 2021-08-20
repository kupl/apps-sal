class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def BS(p, r):
            if r - p <= 1:
                if sum([(n - 1) // p + 1 for n in nums]) <= threshold:
                    return p
                return r
            q = (r + p) // 2
            e = sum([(n - 1) // q + 1 for n in nums])
            if e <= threshold:
                return BS(p, q)
            else:
                return BS(q, r)
        r = max(nums)
        p = 1
        return BS(p, r)
