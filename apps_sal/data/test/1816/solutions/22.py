n = int(input())
f = list(map(int, input().split()))
t = []
for i in range(n):
    t.append((f[i], i))
t = sorted(t, key=lambda x: x[0])
ans = 0
for i in range(1, n):
    ans += abs(t[i][1] - t[i - 1][1])
print(ans)
