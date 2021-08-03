class Solution:
    def knightDialer(self, N: int) -> int:
        steps = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        ret = set()

        def DFS(cur, i):
            if i == N:
                n = 0
                for c in cur:
                    n = n * 10 + c
                ret.add(n)
                print(n)
                return
            for n in steps[cur[-1]]:
                DFS(cur + [n], i + 1)
            return
        for k in list(steps.keys()):
            DFS([k], 1)
        return len(ret)


class Solution:
    def knightDialer(self, N: int) -> int:
        steps = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        dp = [1 for _ in range(10)]
        for _ in range(N - 1):
            cur = [0 for _ in range(10)]
            for i in range(10):
                for j in steps[i]:
                    cur[j] += dp[i]
            dp = cur
        return sum(dp) % (10**9 + 7)
