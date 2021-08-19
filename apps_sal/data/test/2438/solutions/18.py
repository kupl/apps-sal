import sys
input = sys.stdin.readline

n = int(input())
S = input().strip()

A = []
B = []

for i in range(n):
    if S[i] == "A":
        A.append(i)
    else:
        B.append(i)

BE = [-1] * n

for i in range(1, len(A)):
    BE[A[i]] = A[i - 1]

for i in range(1, len(B)):
    BE[B[i]] = B[i - 1]


LEN = n + 10
BIT = [0] * (LEN + 1)


def update(v, w):
    while v <= LEN:
        BIT[v] += w
        v += (v & (-v))


def getvalue(v):
    ANS = 0
    while v != 0:
        ANS += BIT[v]
        v -= (v & (-v))
    return ANS


ANS = 0

for i in range(n):

    if BE[i] != -1:
        update(BE[i] + 1, 1)
        ANS += getvalue(BE[i] + 1)

    # print(i,ANS)

print(ANS)
