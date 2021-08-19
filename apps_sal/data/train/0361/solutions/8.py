class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        res = 0
        dq = deque([[0] * m])
        seen = {tuple([0] * m)}
        while dq:
            length = len(dq)

            for _ in range(length):
                curr = dq.popleft()

                minh = min(curr)
                s = curr.index(minh)
                e = s
                while e + 1 < m and curr[e + 1] == minh:
                    e += 1
                #print(curr, minh, s, e)
                for i in range(min(e - s + 1, n - minh), 0, -1):
                    #print(curr, i)
                    nxt = curr[:]
                    for j in range(s, s + i):
                        nxt[j] += i

                    nxt_state = tuple(nxt)
                    if nxt_state in seen:
                        continue
                    if all(j == n for j in nxt):
                        return res + 1

                    seen.add(nxt_state)
                    dq.append(nxt)

            res += 1
