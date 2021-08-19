import sys
input = sys.stdin.readline

n = int(input())
E = [[] for i in range(n + 1)]
D = dict()
DEG = [0] * (n + 1)
for i in range(n - 1):
    x, y = list(map(int, input().split()))
    E[x].append(y)
    E[y].append(x)
    D[x, y] = i
    D[y, x] = i
    DEG[x] += 1
    DEG[y] += 1

ANS = [-1] * (n - 1)

LIST = []
for i in range(n + 1):
    if DEG[i] == 1:
        LIST.append(i)

if len(LIST) == 2:
    for i in range(n - 1):
        print(i)

else:
    now = 0
    for l in LIST:
        k = E[l][0]
        ANS[D[k, l]] = now
        now += 1

    # print(ANS)

    for i in range(n - 1):
        if ANS[i] == -1:
            ANS[i] = now
            now += 1

    for a in ANS:
        print(a)
