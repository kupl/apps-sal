class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = [i for i in range(lo, hi + 1)]
        powers = [0] * len(nums)
        for i in range(len(nums)):
            cur = nums[i]
            while(cur != 1):
                if cur % 2 == 0:
                    cur = cur / 2
                else:
                    cur = 3 * cur + 1
                powers[i] += 1
        result = [x for _, x in sorted(zip(powers, nums))]
        return result[k - 1]
