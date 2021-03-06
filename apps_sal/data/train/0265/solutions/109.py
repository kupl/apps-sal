class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        hmap = collections.defaultdict(int)
        rsum = 0
        res = 0
        last = -1
        hmap[0] = -1
        for (index, num) in enumerate(nums):
            rsum += num
            csum = rsum - target
            if csum in hmap and hmap[csum] >= last:
                res += 1
                last = index
            hmap[rsum] = index
        return res
