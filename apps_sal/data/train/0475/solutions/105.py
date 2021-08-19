class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        s = []
        for i in range(n):
            t = 0
            for j in range(n - i):
                t += nums[i + j]
                s.append(t)
        mod = 10 ** 9 + 7
        res = 0
        s.sort()
        for i in range(left - 1, right):
            res += s[i] % mod
        return res % mod
