from bisect import *
N = int(input())
L = sorted(map(int, input().split()))
a = 0

for i in range(N):
    for j in range(i + 1, N):
        a += bisect_left(L, L[i] + L[j]) - (j + 1)

print(a)
