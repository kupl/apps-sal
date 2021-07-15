class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        N = 10**9 + 7
        pre = list(itertools.accumulate(nums))
        a = []
        for i in range(n):
            for j in range(i, n):
                a.append(pre[j] - pre[i] + nums[i])
        a = sorted(a)
        return sum(a[left-1:right])%N

