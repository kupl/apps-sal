import sys
input = sys.stdin.readline

n = int(input())
EDGE = [list(map(int, input().split())) for i in range(n)]

CHILDLIST = [[] for i in range(n + 1)]


for i in range(n):
    if EDGE[i][0] == -1:
        continue
    CHILDLIST[EDGE[i][0]].append(i + 1)

ANS = []

for i in range(1, n + 1):
    if EDGE[i - 1][1] == 1:

        for chi in CHILDLIST[i]:
            if EDGE[chi - 1][1] == 0:
                break

        else:
            ANS.append(i)

ANS.sort()
if ANS == []:
    print(-1)
print(*ANS)
