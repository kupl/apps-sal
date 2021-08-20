import math


def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


(N, A, B) = list(map(int, input().split()))
v = sorted(list(map(int, input().split())), reverse=True)
print(sum(v[:A]) / A)
t = v[A - 1]
(m, u) = (0, 0)
for k in range(A):
    if v[k] == t:
        m += 1
for k in range(A, N):
    if v[k] == t:
        u += 1
if m == A:
    ans = 0
    for k in range(A, min(A + u + 1, B + 1)):
        ans += nCr(m + u, k)
    print(ans)
else:
    print(nCr(m + u, m))
