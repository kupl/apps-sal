import sys
input = sys.stdin.readline
n = int(input())
S = input().strip()
LIST = [[] for i in range(26)]
for i in range(n):
    LIST[ord(S[i]) - 97].append(i)
LEN = n + 1
BIT = [0] * (LEN + 1)


def update(v, w):
    while v <= LEN:
        BIT[v] += w
        v += v & -v


def getvalue(v):
    ANS = 0
    while v != 0:
        ANS += BIT[v]
        v -= v & -v
    return ANS


ANS = 0
moji = [0] * 26
for i in range(n - 1, -1, -1):
    s = ord(S[i]) - 97
    x = LIST[s][moji[s]]
    ANS += x - getvalue(x + 1)
    moji[s] += 1
    update(x + 1, 1)
print(ANS)
