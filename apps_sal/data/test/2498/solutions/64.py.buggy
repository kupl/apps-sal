import math


def n_2(n):
    c = 0
    while n % 2 == 0:
        c += 1
        n >>= 1
    return (n, c)


N, M = map(int, input().split())
A = list(map(int, input().split()))
A[0], a = n_2(A[0])
p = False
for i in range(1, N):
    A[i], b = n_2(A[i])
    if a != b:
        p = True
        break
if p:
    print(0)
    return
n = 1
for _ in range(a - 1):
    n *= 2
l = n
for a in A:
    l = l * a // math.gcd(l, a)
ans = M // l - M // (2 * l)
print(ans)
