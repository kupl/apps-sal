class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        indx = 0
        while indx <= n:
            add = 0
            for i in range(indx, n):
                add += sum(nums[indx:i + 1])
                ans.append(add)
                add = 0
            indx += 1
        ans.sort()
        return sum(ans[left - 1:right]) % (10 ** 9 + 7)
