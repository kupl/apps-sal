class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        a = []
        for i in range(n):
            prev = 0
            for j in range(i, n):
                prev += nums[j]
                a.append(prev)
        a.sort()
        # print(a)
        return sum(a[left-1:right]) % (10**9 +7)
