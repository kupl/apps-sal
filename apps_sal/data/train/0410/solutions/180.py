class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = dict()
        dp[0] = dp[2] = 1
        dp[1] = 0

        def calc(x, adj):
            if x % 2 == 0:
                n = x // 2
            else:
                n = 3 * x + 1
            if dp.get(n) is None:
                adj.append(n)
                calc(n, adj)
            else:
                count = dp.get(n)
                for a in adj[::-1]:
                    count += 1
                    dp[a] = count

        to_sort = []
        for i in range(lo, hi + 1):
            calc(i, [i])
            to_sort.append([i, dp.get(i)])
        sorted_res = sorted(to_sort, key=lambda x: x[1])
        return sorted_res[k - 1][0]
