n = int(input())
socks = list(map(int, input().split()))
f = [0] * (n + 1)
cur = 0
ans = 0
for s in socks:
    if f[s] == 1:
        cur -= 1
    else:
        cur += 1
        f[s] = 1
    ans = max(ans, cur)
print(ans)
