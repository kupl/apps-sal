class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        a = []
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                a.append(s)
        a = sorted(a)
        b = 10**9 + 7
        print(b)
        a = sum(a[left - 1:right])
        if a > b:
            return a % b
        else:
            return a
