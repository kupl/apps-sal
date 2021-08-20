from collections import Counter


class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        d = Counter()
        c = []
        e = []
        for i in A:
            if i < 0:
                c.append(i)
            elif i >= 0:
                e.append(i)
        c.sort(reverse=True)
        c.extend(e)
        A = c
        print(A)
        for i in A:
            d[i] += 1
        if d[0] % 2 != 0:
            return False
        d[0] = 0
        for i in A:
            if 2 * i in d and d[i] <= d[2 * i]:
                d[2 * i] -= d[i]
                d[i] = 0
            elif d[i] == 0:
                continue
            else:
                return False
        return True
