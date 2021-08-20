class Solution:

    def minDays(self, n: int) -> int:
        ans = 1
        bfs = [n]
        seen = set()
        while bfs:
            bfs2 = []
            for x in bfs:
                if x == 1:
                    return ans
                seen.add(x)
                if x - 1 not in seen:
                    bfs2.append(x - 1)
                if x % 2 == 0 and x // 2 not in seen:
                    bfs2.append(x // 2)
                if x % 3 == 0 and x // 3 not in seen:
                    bfs2.append(x // 3)
            ans += 1
            bfs = bfs2
