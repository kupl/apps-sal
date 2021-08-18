import sys
input = sys.stdin.readline

n, k, m = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort()

SUM = sum(A)
ANS = 0
for i in range(min(n, m + 1)):
    MPOWER = SUM + min(m - i, (n - i) * k)
    ANS = max(ANS, MPOWER / (n - i))

    SUM -= A[i]


print(ANS)
