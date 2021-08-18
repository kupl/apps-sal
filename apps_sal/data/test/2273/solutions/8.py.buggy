import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
E = [set() for i in range(n + 1)]
ECOUNT = [0] * (n + 1)

for i in range(m):
    x, y = list(map(int, input().split()))
    E[x].add(y)
    E[y].add(x)
    ECOUNT[x] += 1
    ECOUNT[y] += 1


Group = [i for i in range(n + 1)]


def find(x):
    while Group[x] != x:
        x = Group[x]
    return x


def Union(x, y):
    if find(x) != find(y):
        Group[find(y)] = Group[find(x)] = min(find(y), find(x))


SCORE = 0
for i in range(1, n + 1):
    if find(i) == i:
        SCORE += 1
        if SCORE >= 6:
            print(-1)
            return

        for j in range(i + 1, n + 1):
            if j in E[i]:
                continue
            else:
                Union(i, j)

FD = [find(i) for i in range(n + 1)]
if len(set(FD[1:])) != 3:
    print(-1)
    return

for i in range(n + 1):
    for j in E[i]:
        if FD[i] == FD[j]:
            print(-1)
            return


compression_dict = {a: ind for ind, a in enumerate(sorted(set(FD)))}
ANS = [compression_dict[a] for a in FD]

VFD = [0, 0, 0]
EFD = [0, 0, 0]
for i in range(1, n + 1):
    VFD[ANS[i] - 1] += 1
    EFD[ANS[i] - 1] += ECOUNT[i]

for i in range(3):
    VS = 0
    for j in range(3):
        if i == j:
            continue
        VS += VFD[i] * VFD[j]

    if EFD[i] == VS:
        continue
    else:
        print(-1)
        return


print(*ANS[1:])
