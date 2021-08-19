import math


class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        md = 10**9 + 7
        p = A * B // math.gcd(A, B)
        np = p // A + p // B - 1
        n1 = N // np
        res = n1 * (p % md) % md
        n2 = N % np
        i, j, curr = 0, 0, 0
        while i + j < n2:
            if A * (i + 1) < B * (j + 1):
                i += 1
                curr = A * i
            else:
                j += 1
                curr = B * j
        res = (res + curr) % md
        # print(i,j,n1,n2,np)
        return res
