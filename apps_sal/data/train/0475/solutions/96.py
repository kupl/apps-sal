class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = list()
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                ans.append(s)
        ans = sorted(ans)
        # print(ans)
        res = 0
        for i in ans[left - 1:right]:
            res += i
        return res % (7 + (10**9))
