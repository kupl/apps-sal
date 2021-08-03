from math import log2
t = int(input())

for _ in range(t):
    n = int(input())
    k = int(log2(n))
    ans = n * (n + 1) // 2  # sum all from 1 to n
    ans -= 2 * (2**(k + 1) - 1)  # subtract twice sum of 2^n for n from 0 to k

    print(ans)
