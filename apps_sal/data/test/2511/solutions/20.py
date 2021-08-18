n, k = map(int, input().split())
ans = k
mod = 10**9 + 7
v = [[0] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)
if n == 1:
    print(k)
elif n == 2:
    print(k * (k - 1))
else:
    q = [1]
    v[1][0] = 1
    while q:
        t = q.pop()
        cnt = 2 - (t == 1)
        for i in range(1, len(v[t])):
            if v[v[t][i]][0] == 0:
                q.append(v[t][i])
                v[v[t][i]][0] = 1
                ans = (ans * (k - cnt)) % mod
                cnt += 1
    print(ans)
