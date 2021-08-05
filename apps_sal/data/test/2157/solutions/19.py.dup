import sys
data = [int(i) for i in sys.stdin.read().split()]
data.reverse()
def read(): return data.pop()


n, q = read(), read()
A = [read() for i in range(n)]
F = [0] * (n + 5)

for i in range(q):
    l, r = read(), read()
    F[l] += 1
    F[r + 1] -= 1

for i in range(1, n + 1):
    F[i] += F[i - 1]

A.sort()
F = sorted(F[1:n + 1])

ans = 0
for i in range(n):
    ans += A[i] * F[i]

print(ans)
