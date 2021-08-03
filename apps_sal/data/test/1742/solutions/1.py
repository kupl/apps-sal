import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
P = list(map(int, input().split()))
PAIR = [list(map(int, input().split())) for i in range(m)]

NAT = P[-1]

LIST = [[] for i in range(n + 1)]

for x, y in PAIR:
    LIST[x].append(y)

for i in range(n + 1):
    LIST[i] = set(LIST[i])

FLIST = [NAT]
i = n - 2
ANS = 0
while i >= 0:

    for j in FLIST:
        if j in LIST[P[i]]:
            continue
        else:
            FLIST.append(P[i])
            break

    else:
        ANS += 1

    i -= 1

print(ANS)
