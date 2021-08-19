class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l = len(nums)
        a = [[0 for x in range(l)] for y in range(l)]
        s = 0
        t = []
        MOD = 1000000007
        for i in range(0, l):
            s = s + nums[i]
            a[0][i] = s
            t.append(a[0][i])
        for i in range(1, l):
            a[i][l - 1] = s - a[0][i - 1]
            t.append(a[i][l - 1])
        for i in range(1, l):
            for j in range(i, l - 1):
                a[i][j] = s - a[0][i - 1] - a[j + 1][l - 1]
                t.append(a[i][j])
        t.sort()
        b = 0
        for i in range(left - 1, right):
            b = (b + t[i]) % MOD
        return b
