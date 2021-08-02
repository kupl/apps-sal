import sys
sys.setrecursionlimit(10**9)
l = list(input())
n = len(l)
p = 10**9 + 7
ans = 0
d = 0


def f(n, k, q):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return ((f(n, k // 2, q))**2) % q
    else:
        return (n * f(n, k - 1, q)) % q


for i in range(n):
    if l[i] == "1":
        x = n - i - 1
        ans += (f(3, x, p) * f(2, d, p)) % p
        d += 1
    else:
        continue

ans += f(2, d, p)
print((ans % p))
