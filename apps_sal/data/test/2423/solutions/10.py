n = int(input())
tun = {}
for i in range(n):
    tun[i + 1] = 0
for i in range(n - 1):
    u, v = map(int, input().split())
    tun[u] += 1
    tun[v] += 1
ans = 0
for i in range(1, n + 1):
    if tun[i] == 1:
        ans += 1
print(ans)
