class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        M = 10**9 + 7
        
        table = [-1]
        pos, cnd = 1, 0
        while pos < len(evil):
            if evil[pos] == evil[cnd]:
                table.append(table[cnd])
            else:
                table.append(cnd)
                cnd = table[cnd]
                while cnd >= 0 and evil[pos] != evil[cnd]:
                    cnd = table[cnd]
            pos += 1
            cnd += 1
        table.append(cnd)
        
        @lru_cache(None)
        def dfs(i, j, u, b):
            if j == len(evil):
                return 0
            if i == n:
                return 1
            r = 0
            for c in range(ord(s1[i]) if b else 97, ord(s2[i])+1 if u else 123):
                if c == ord(evil[j]):
                    t = dfs(i+1, j+1, u and c == ord(s2[i]), b and c == ord(s1[i]))
                else:
                    p = j
                    while p >= 0:
                        if ord(evil[p]) == c:
                            break
                        p = table[p]
                    t = dfs(i+1, p+1, u and c == ord(s2[i]), b and c == ord(s1[i]))
                r += t
            return r % M
        
        return dfs(0, 0, True, True)
