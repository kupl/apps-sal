class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        xs = [i for (i, n) in enumerate(nums) if n]
        return all((y - x > k for (x, y) in zip(xs, xs[1:])))
