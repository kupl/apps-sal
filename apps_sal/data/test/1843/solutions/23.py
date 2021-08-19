from math import log2
t = int(input())
for _ in range(t):
    n = int(input())
    k = int(log2(n))
    ans = n * (n + 1) // 2
    ans -= 2 * (2 ** (k + 1) - 1)
    print(ans)
