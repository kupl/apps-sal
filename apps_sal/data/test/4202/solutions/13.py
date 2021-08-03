l, r = map(int, input().split())
ans = float("INF")
mod = 2019

for i in range(l, r + 1):
    if i == l + 2019 or ans == 0:
        break
    for j in range(l, r + 1):
        if j == l + 2019:
            break
        if i == j:
            continue
        ans = min(ans, (i * j) % mod)
print(ans)
