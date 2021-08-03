class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new = []
        for i in range(len(nums)):
            n = 0
            for j in range(i, len(nums)):
                n += nums[j]
                new.append(n)
        new.sort()
        ans = 0
        for i in range(left - 1, right):
            ans += new[i]
        ans = ans % (10**9 + 7)
        return ans
