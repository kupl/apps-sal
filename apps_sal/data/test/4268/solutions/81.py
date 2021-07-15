n, d = list(map(int, input().split()))
x = [[0 for j in range(d)]for i in range(n)]
for i in range(n):
    x[i] = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k]) ** 2
        dist = dist**(1/2)
        if dist - int(dist) == 0:
            ans += 1
print(ans)

