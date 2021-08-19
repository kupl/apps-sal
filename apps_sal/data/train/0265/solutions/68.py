class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        N = len(nums)

        rtv = 0

        presum = dict()
        presum[0] = -1
        total = 0
        for i, v in enumerate(nums):
            total += v

            ne = total - target
            if ne in presum and presum[ne] < i:
                rtv += 1
                # print(\"{} {}\".format(presum[ne]+1, i))

                presum = dict()
                presum[0] = i
                total = 0
            else:
                presum[total] = i

        return rtv
