from collections import defaultdict


class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        M = 10 ** 9 + 7
        q = {(-1, 0): 1}
        for _ in range(n):
            p = defaultdict(lambda: 0)
            for (x, r) in q:
                for y in range(6):
                    if y == x:
                        if r + 1 <= rollMax[y]:
                            p[y, r + 1] += q[x, r] % M
                    else:
                        p[y, 1] += q[x, r] % M
            q = p
        return sum(q.values()) % M
