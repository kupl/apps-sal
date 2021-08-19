class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        l = len(nums)
        for i in range(l):
            summ = 0
            for j in nums[i:]:
                summ += j
                res.append(summ)
        res.sort()
        ans = sum(res[left - 1:right])
        return int(ans % (10 ** 9 + 7))
