class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        rangeSum = []
        mod = 10 ** 9 + 7

        for i in range(n):
            rangeSum.append(nums[i])
            for j in range(i):
                rangeSum.append(sum(nums[j:i]) + nums[i])

            #print (rangeSum)

        rangeSum.sort()

        ans = 0
        for i in range(left - 1, right):
            ans += rangeSum[i] % mod

        return ans % mod
