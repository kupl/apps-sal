from bisect import bisect
import random


def binary_search(L, n, i, j):
    low = i
    high = j

    while low <= high:
        mid = (low + high) // 2
        guess = L[mid]
        if guess > n:
            high = mid - 1
        else:
            low = mid + 1
    return low


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ans = 0
i, j = 0, 0

A_ind = []
B_cum = [0]

for a in A:
    i = bisect(B, a)
    A_ind.append(i)

s = 0
for b in B:
    j = i = bisect(C, b)
    s += N - j
    B_cum.append(s)

for a in A_ind:
    ans += B_cum[-1] - B_cum[a]
print(ans)
