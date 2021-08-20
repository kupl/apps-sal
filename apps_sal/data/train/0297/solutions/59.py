class Solution:

    def numTilePossibilities(self, s: str) -> int:
        (ans, C) = (0, Counter(s))

        def dfs(C, cur):
            nonlocal ans
            if cur:
                ans += 1
            if not C:
                return
            C1 = C.copy()
            for x in C:
                cur.append(x)
                C1[x] -= 1
                if C1[x] == 0:
                    del C1[x]
                dfs(C1, cur)
                cur.pop()
                C1[x] += 1
        dfs(C, cur=[])
        return ans
