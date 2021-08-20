from bisect import *
N = int(input())
(*L,) = sorted(map(int, input().split()))
r = 0
for a in range(N):
    for b in range(a + 1, N):
        x = L[a]
        y = L[b]
        r += max(0, bisect_left(L, x + y) - (b + 1))
print(r)
