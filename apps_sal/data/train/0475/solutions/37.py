class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        L = len(nums)
        for i in range(L):
            for j in range(i + 1, L + 1):
                ans.append(sum(nums[i:j]))
        ans.sort()
        return sum(ans[left - 1:right]) % (10 ** 9 + 7)
