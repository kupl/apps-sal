class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        r1 = []
        r2 = []
        for i in range(1, int(n**.5) + 1):
            if n % i == 0:
                r1.append(i)
                if n != i * i:
                    r2 = [n // i] + r2
        r = r1 + r2
        if len(r) < k:
            return -1
        else:
            return r[k - 1]
