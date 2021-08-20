class Solution:

    def getKth(self, a: int, b: int, k: int) -> int:

        def fun(x, d):
            if x == 1:
                return 0
            if x % 2 == 0:
                if x // 2 in d:
                    d[x] = d[x // 2] + 1
                else:
                    d[x] = fun(x // 2, d) + 1
            elif 3 * x + 1 in d:
                d[x] = d[3 * x + 1] + 1
            else:
                d[x] = fun(3 * x + 1, d) + 1
            return d[x]
        d = {}
        for i in range(a, b + 1):
            fun(i, d)
        d[1] = 0
        ans = []
        for i in range(a, b + 1):
            ans.append((d[i], i))
        ans.sort()
        return ans[k - 1][1]
