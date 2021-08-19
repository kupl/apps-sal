import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
Group = [i for i in range(n + 1)]
Nodes = [1] * (n + 1)


def find(x):
    while Group[x] != x:
        x = Group[x]
    return x


def Union(x, y):
    if find(x) != find(y):
        if Nodes[find(x)] < Nodes[find(y)]:
            Nodes[find(y)] += Nodes[find(x)]
            Nodes[find(x)] = 0
            Group[find(x)] = find(y)
        else:
            Nodes[find(x)] += Nodes[find(y)]
            Nodes[find(y)] = 0
            Group[find(y)] = find(x)


for i in range(m):
    (x, y) = list(map(int, input().split()))
    Union(x, y)
MINI = [i for i in range(n + 1)]
for i in range(n + 1):
    MINI[find(i)] = min(MINI[find(i)], i)
ANS = 0
MIN = n
ANS = 0
for i in range(n, 0, -1):
    if MIN < MINI[find(i)]:
        MINI[find(i)] = min(MINI[find(i)], MINI[find(MIN)])
        Union(MIN, i)
        ANS += 1
    else:
        MIN = MINI[find(i)]
print(ANS)
