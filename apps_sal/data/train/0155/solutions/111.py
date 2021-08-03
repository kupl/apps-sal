class Solution:
    def rec(self, v):
        if self.memo[v] != -1:
            return self.memo[v]

        res = 1

        for nv in self.G[v]:
            res = max(res, 1 + self.rec(nv))

        self.memo[v] = res
        return res

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        self.G = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                self.G[i].append(j)

            for j in range(i + 1, i + d + 1):
                if j >= n or arr[j] >= arr[i]:
                    break
                self.G[i].append(j)

        self.memo = [-1] * n
        ans = 0

        for i in range(n):
            ans = max(ans, self.rec(i))

        return ans
