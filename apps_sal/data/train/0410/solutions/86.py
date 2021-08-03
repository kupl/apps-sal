class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getPow(n):
            c = 0
            while n != 1:
                if n % 2 == 0:
                    n //= 2
                else:
                    n = 3 * n + 1
                c += 1
            return c

        def func():
            arr = {i: getPow(i) for i in range(lo, hi + 1)}
            v = list(set(arr.values()))
            v.sort()
            fin = []
            for i in v:
                t = []
                for a, b in arr.items():
                    if b == i:
                        t.append(a)
                t.sort()
                fin.extend(t)
            return fin[k - 1]
        return func()
