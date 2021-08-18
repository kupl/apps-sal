n = input()
n = int(n)
a = input()
a = a.split()
a[0:0] = [0]
for i in range(1, n + 1):
    a[i] = int(a[i])
e = [[]for i in range(0, n + 1)]
for i in range(2, n + 1):
    x = input()
    x = x.split()
    e[i].append([int(x[0]), int(x[1])])
    e[int(x[0])].append([i, int(x[1])])
q = [1]
cnt = 0
f = [0 for i in range(0, n + 1)]
dp = [0 for i in range(0, n + 1)]
ans = 1
while cnt < len(q):
    now = q[cnt]
    cnt += 1
    for x in e[now]:
        if x[0] != f[now]:
            f[x[0]] = now
            dp[x[0]] = max(x[1] + dp[now], 0)
            if dp[x[0]] > a[x[0]]:
                continue
            q.append(x[0])
            ans += 1
print(n - ans)
