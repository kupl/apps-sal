import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
x = int(input())

ASUM = [0]
BSUM = [0]

for i in range(n):
    ASUM.append(A[i] + ASUM[-1])
for i in range(m):
    BSUM.append(B[i] + BSUM[-1])


ALIST = dict()
BLIST = dict()

for i in range(n + 1):
    for j in range(i + 1, n + 1):
        if ALIST.get(j - i, 10**15) > ASUM[j] - ASUM[i]:
            ALIST[j - i] = ASUM[j] - ASUM[i]

for i in range(m + 1):
    for j in range(i + 1, m + 1):
        if BLIST.get(j - i, 10**15) > BSUM[j] - BSUM[i]:
            BLIST[j - i] = BSUM[j] - BSUM[i]

ANS = 0
for i in ALIST:
    for j in BLIST:
        if ALIST[i] * BLIST[j] <= x and i * j > ANS:
            ANS = i * j

print(ANS)
