import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
X = list(map(int, input().split()))

SET = set(X)
dis = 1

ANS = []
MSET = set(X)
PSET = set(X)
score = 0
MEM = 0

while MEM < m:

    REMLIST = []
    for t in MSET:
        if t - dis in SET:
            REMLIST.append(t)
        else:
            ANS.append(t - dis)
            SET.add(t - dis)
            MEM += 1
            score += dis

        if MEM == m:
            break

    MSET -= set(REMLIST)

    if MEM == m:
        break

    REMLIST = []
    for t in PSET:
        if t + dis in SET:
            REMLIST.append(t)
        else:
            ANS.append(t + dis)
            SET.add(t + dis)
            MEM += 1
            score += dis

        if MEM == m:
            break

    PSET -= set(REMLIST)
    dis += 1

print(score)
print(*ANS)
