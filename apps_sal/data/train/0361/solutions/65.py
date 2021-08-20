class Solution:

    def tilingRectangle(self, m: int, n: int) -> int:
        cur = [0] * (n * m)
        q = [cur]
        step = 0
        seen = {tuple(cur)}
        while q and step < n * m + 1:
            step += 1
            nex = []
            for cur in q:
                found = True
                for i in range(m):
                    for j in range(n):
                        if cur[i * n + j] == 0:
                            start = [i, j]
                            found = False
                            break
                    if not found:
                        break
                if found:
                    return step - 1
                while j + 1 < n and cur[i * n + j + 1] == 0:
                    j += 1
                k = j - start[1] + 1
                for sz in range(1, k + 1):
                    cc = cur.copy()
                    flag = False
                    for i in range(start[0], start[0] + sz):
                        for j in range(start[1], start[1] + sz):
                            if not (0 <= i < m and 0 <= j < n and (cur[i * n + j] == 0)):
                                flag = True
                                break
                            cc[i * n + j] = 1
                        if flag:
                            break
                    if flag:
                        break
                    C = tuple(cc)
                    if C not in seen:
                        seen.add(C)
                        nex.append(cc)
            q = nex
