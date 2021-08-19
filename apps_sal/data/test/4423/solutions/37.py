n = int(input())
sp = [input().split() for i in range(n)]
for i in range(n):
    sp[i][1] = int(sp[i][1])
    sp[i].append(i + 1)
sp.sort()
for i in range(100):
    for j in range(1, n):
        if sp[j][0] == sp[j - 1][0]:
            if sp[j][1] > sp[j - 1][1]:
                (sp[j - 1], sp[j]) = (sp[j], sp[j - 1])
for i in range(n):
    print(sp[i][2])
