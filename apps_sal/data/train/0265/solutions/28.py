class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        psum = [0]
        for v in nums:
            psum.append(v + psum[-1])

        def helper(lo, target):
            d = {psum[lo - 1]}
            ans = 0
            for i in range(lo, len(psum)):
                if psum[i] - target in d:
                    ans = 1 + helper(i + 1, target)
                    break
                d.add(psum[i])
            return ans
        return helper(1, target)
