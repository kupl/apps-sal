n = int(input())
d = {}
for _ in range(n):
    a = input().split()
    if a[0] in d:
        for i in range(int(a[1])):
            d[a[0]].append(a[2 + i])
        continue
    d[a[0]] = []
    for i in range(int(a[1])):
        d[a[0]].append(a[2 + i])
print(len(d))
for i in d:
    for j in range(len(d[i])):
        for k in range(len(d[i])):
            if j != k and d[i][k].endswith(d[i][j]):
                d[i][j] = 'a'
    print(i, len([e for e in d[i] if e != 'a']), end=' ')
    for g in d[i]:
        if g != 'a':
            print(g, end=' ')
    print()
