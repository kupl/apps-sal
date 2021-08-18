import sys
input = sys.stdin.readline

n, x = list(map(int, input().split()))
A = list(map(int, input().split()))

SUM = [0]

for a in A:
    SUM.append(SUM[-1] + a)

MAXLIST = [SUM[0]]
MINLIST = [SUM[0]]

for i in range(1, n + 1):
    MAXLIST.append(max(MAXLIST[-1], SUM[i]))
    MINLIST.append(min(MINLIST[-1], SUM[i]))

MAXLIST_INV = [SUM[-1]]
MINLIST_INV = [SUM[-1]]

for i in range(n - 1, -1, -1):
    MAXLIST_INV.append(max(MAXLIST_INV[-1], SUM[i]))
    MINLIST_INV.append(min(MINLIST_INV[-1], SUM[i]))

MAXLIST_INV = MAXLIST_INV[::-1]
MINLIST_INV = MINLIST_INV[::-1]


if x > 0:

    ANS = 0

    for i in range(n + 1):
        base = SUM[i]
        MINUS = MINLIST[i]

        ANS = max(ANS, (base - MINUS) * x)

    print(ANS)

else:

    ANS = 0
    MAX = 0
    MIN = 0
    MINUS = 0
    NOWMINUS = 0

    for i in range(n + 1):
        base = SUM[i]
        PLUS = MAXLIST_INV[i]

        ANS = max(ANS, NOWMINUS + PLUS - base + base * x)

        MIN = min(MIN, SUM[i])

        if NOWMINUS <= SUM[i] - MIN + SUM[i] * (-x):
            NOWMINUS = SUM[i] - MIN + SUM[i] * (-x)
            MAX = SUM[i]

    print(ANS)
