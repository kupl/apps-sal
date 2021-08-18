class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            return self.tilingRectangle(m, n)
        ans = n * m
        h = [0] * n

        def getmin(l):
            minv = 100000
            mini = -1
            for i in range(len(l)):
                if l[i] < minv:
                    minv = l[i]
                    mini = i
            return minv, mini

        def dfs(cur):
            nonlocal ans
            if cur >= ans:
                return

            it, iti = getmin(h)
            if it == m:
                ans = cur
                return

            low = it
            s = iti
            e = s
            while e < n and h[e] == h[s] and (e - s + 1) <= (m - low):
                e += 1
            e -= 1
            for i in range(e, s - 1, -1):
                size = i - s + 1
                for j in range(s, i + 1):
                    h[j] += size
                dfs(cur + 1)
                for j in range(s, i + 1):
                    h[j] -= size

        dfs(0)
        return ans
