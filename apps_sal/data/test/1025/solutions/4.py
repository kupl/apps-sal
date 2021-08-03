from fractions import *
n = int(input())
s = n * (n - 1) * (n - 2) // 6
p = [list(map(int, input().split()))for _ in range(n)]
def f(a, b): return a // gcd(a, b) + (b // gcd(a, b) << 20)


for i in range(n):
    k, l = 0, sorted(f(p[i][0] - X, p[i][1] - Y)for X, Y in p[:i])
    for j in range(1, i):
        k = k + 1 if l[j] == l[j - 1]else 0
        s -= k
print(s)
