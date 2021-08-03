from typing import Set


class myset(object):

    def __init__(self, maxi):
        self.s = [i for i in range(0, maxi + 1)]
        self.l = [1] * (maxi + 1)

    def find(self, x):
        if self.s[x] != x:
            self.s[x] = self.find(self.s[x])

        return self.s[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return px

        if px > py:
            px, py = py, px

        self.s[px] = self.s[py]
        self.l[py] += self.l[px]

        return py


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        d: Dict[int][int] = {}
        p: List[int] = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]

        def pf(x: int) -> List[int]:
            result: Set[int] = set()
            i: int = 0
            n: int = 2
            while x >= n * n:
                if x % n == 0:
                    result.add(n)
                    x = x // n
                else:
                    n += 1
            result.add(x)

            return list(result)

        if not A:
            return 0

        s = myset(max(A))

        mypf: List[int]
        for a in A:
            mypf = pf(a)
            print(mypf)
            d[a] = mypf[0]
            for i in range(len(mypf) - 1):
                s.union(mypf[i], mypf[i + 1])

        count = {}
        maxi: int = 0
        for a in A:
            id: int = s.find(d[a])
            if id in count:
                count[id] += 1
            else:
                count[id] = 1
            maxi = max(maxi, count[id])

        return maxi
