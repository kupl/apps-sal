n, m, k = list(map(int,input().split()))
x = []
for i in range(m+1):
    x.append(int(input()))
fedor = x[m]
ans = 0
for i in range(m):
    fr = x[i]
    fed = fedor
    count = 0
    while fr > 0 or fed > 0:
        count += (fr%2 + fed%2) % 2
        fr //= 2
        fed //= 2
    if count <= k:
        ans += 1
print(ans)

