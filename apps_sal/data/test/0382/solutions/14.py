import sys

n, m, q = list(map(int, input().split()))
s = input()
t = input()
A = [None] * q
for i in range(q):
    A[i] = list(map(int, input().split()))

if m > n:
    for i in range(q):
        print(0)

    return

score = [0 for i in range(n - m + 1)]
for i in range(n - m + 1):
    if t == s[i:i + m]:
        score[i] = 1

SUM = [0 for i in range(n - m + 1)]
SUM[0] = score[0]
for i in range(1, n - m + 1):
    SUM[i] = score[i] + SUM[i - 1]


SUM = [0] + SUM
for i in range(q):
    if A[i][1] - m + 1 <= A[i][0] - 1:
        print(0)
    else:
        print(SUM[A[i][1] - m + 1] - SUM[A[i][0] - 1])
