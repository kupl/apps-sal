n = int(input())
d = [0] * (n + 1)
for i in range(n - 1):
    u, v = list(map(int, input().split()))
    d[u] += 1
    d[v] += 1
ans = 0
for i in range(n):
    if d[i + 1] == 2:
        ans += 1
if ans == 0:
    print("YES")
else:
    print("NO")

