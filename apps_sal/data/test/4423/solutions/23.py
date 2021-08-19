n = int(input())
sp = list([input().split() for i in range(n)])
sp2 = [[i] + sp[i] for i in range(n)]
ans = sorted(sp2, key=lambda x: int(x[2]), reverse=True)
ans2 = sorted(ans, key=lambda x: x[1])
for i in range(n):
    print(ans2[i][0] + 1)
