class Solution:
    def minOperations(self, nums: List[int]) -> int:
        f = {}

        def calc(x):
            if x == 0:
                return 0, 0
            if x not in f:
                if x % 2 == 1:
                    a, b = calc(x - 1)
                    f[x] = (a + 1, b)
                else:
                    a, b = calc(x // 2)
                    f[x] = (a, b + 1)
            return f[x]

        x = []
        y = []
        for e in nums:
            a, b = calc(e)
            x.append(a)
            y.append(b)
        return sum(x) + max(y)
