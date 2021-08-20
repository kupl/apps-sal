from bisect import bisect_left
N = int(input())
A = [int(input()) for _ in range(N)]
L = [-1] * N
for a in A:
    idx = bisect_left(L, a)
    L[idx - 1] = a
print(N - L.count(-1))
