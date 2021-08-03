from math import log
N = int(input())
A = [int(i) for i in input().split()]
d = {}
for i in A:
    d[i] = d.setdefault(i, 0) + 1

l = int(log(max(A)) / log(2)) + 2
ans = 0
for i in range(N):
    for j in range(1, l):
        c = (1 << j) - A[i]
        ans += d.get(c, 0)
        ans -= c == A[i]

print(ans // 2)
