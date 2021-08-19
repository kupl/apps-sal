from bisect import bisect
import random


def binary_search(L, n, i, j):
    # print(L, n, i, j)
    low = i
    high = j

    while low <= high:
        mid = (low + high) // 2
        guess = L[mid]
        # if guess == n:
        # return mid
        if guess > n:
            high = mid - 1
        else:
            low = mid + 1
    # print(low)
    return low


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
# N = 10 ** 5
# A = [random.randint(1, 10**9) for _ in range(N)]
# B = [random.randint(1, 10**9) for _ in range(N)]
# C = [random.randint(1, 10**9) for _ in range(N)]

A.sort()
B.sort()
C.sort()

ans = 0
i, j = 0, 0

A_ind = []
B_cum = [0]

for a in A:
    # i = binary_search(B, a, i, N-1)
    i = bisect(B, a)
    A_ind.append(i)

s = 0
for b in B:
    # j = binary_search(C, b, j, N-1)
    j = i = bisect(C, b)
    s += N - j
    B_cum.append(s)

for a in A_ind:
    ans += B_cum[-1] - B_cum[a]
print(ans)
