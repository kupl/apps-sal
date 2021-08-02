from bisect import *
N = int(input())
*L, = sorted(map(int, input().split()))

r = 0
for a in range(N):
    r += sum(bisect_left(L, L[a] + L[b]) - (b + 1) for b in range(a + 1, N))
print(r)
