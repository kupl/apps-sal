n = int(input())
ans = 0
al = []
xy = [[] for _ in range(n)]
for k in range(n):
    a = int(input())
    al.append(a)
    for l in range(a):
        x, y = list(map(int, input().split()))
        xy[k].append([x, y])
for i in range(2**n):
    kinds = [0] * n
    jud = 1
    for j in range(n):
        if (i >> j) & 1:
            kinds[j] = 1
    for k in range(n):
        if kinds[k] == 1:
            a = al[k]
            for l in range(a):
                x = xy[k][l][0]
                y = xy[k][l][1]
                if kinds[x - 1] != y:
                    jud = 0
    if jud == 1:
        ans = max(ans, kinds.count(1))
print(ans)
