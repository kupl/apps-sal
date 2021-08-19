(n, d) = list(map(int, input().split()))
x = []
for i in range(n):
    p = list(map(int, input().split()))
    x.append(p)
ans = 0
for i in range(len(x) - 1):
    for j in range(i + 1, len(x)):
        dis = 0
        for k in range(d):
            dis += (x[i][k] - x[j][k]) ** 2
        if int(dis ** (1 / 2)) == dis ** (1 / 2):
            ans += 1
print(ans)
