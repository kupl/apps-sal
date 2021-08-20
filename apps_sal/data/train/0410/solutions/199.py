class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = collections.defaultdict(int)
        d[1] = 0
        d[2] = 1

        def dfs(num):
            if num in d:
                return d[num]
            count = 0
            if num % 2:
                d[num] = 1 + dfs(num * 3 + 1)
                return 1 + dfs(num * 3 + 1)
            if not num % 2:
                d[num] = 1 + dfs(num // 2)
                return 1 + dfs(num // 2)
        res = collections.defaultdict(int)
        for n in range(lo, hi + 1):
            res[n] = dfs(n)
        res = sorted(list(res.items()), key=lambda x: x[1])
        return res[k - 1][0]
