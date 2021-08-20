n = int(input())
sp = [[] for _ in range(n)]
for i in range(n):
    sp[i] = list(input().split())
    sp[i].append(i + 1)
ssp = sorted(sp, key=lambda x: (x[0], -int(x[1])))
for i in range(n):
    print(ssp[i][2])
