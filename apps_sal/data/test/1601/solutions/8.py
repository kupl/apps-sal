from sys import stdin
input = stdin.readline
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
a = [[l[i], i + 1] for i in range(n)]
used = [0] * (n + 1)
a.sort()
d = {}
for i in a:
    d[i[0][0]] = []
for i in a:
    d[i[0][0]].append([i[0][1], i[0][2], i[1]])
for x in d:
    l = d[x]
    b = {}
    for i in l:
        b[i[0]] = []
    for i in l:
        b[i[0]].append([i[1], i[2]])
    for y in b:
        pom = 0
        while pom + 1 < len(b[y]):
            print(b[y][pom][1], b[y][pom + 1][1])
            used[b[y][pom][1]] = 1
            used[b[y][pom + 1][1]] = 1
            pom += 2
    c = []
    for gg in l:
        if used[gg[2]] == 0:
            c.append(gg)
    cc = [[c[gg][0], c[gg][2]] for gg in range(len(c))]
    g = 0
    while g < len(cc) - 1:
        print(cc[g][-1], cc[g + 1][-1])
        used[cc[g][-1]] = 1
        used[cc[g + 1][-1]] = 1
        g += 2
c = []
for i in range(0, n):
    if used[a[i][1]] == 0:
        c.append([a[i][0][0], a[i][1]])
c.sort()
i = 0
while i < len(c) - 1:
    print(c[i][1], c[i + 1][1])
    i += 2
