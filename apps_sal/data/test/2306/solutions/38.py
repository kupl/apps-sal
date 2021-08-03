n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
T = sum(t) * 2
kukan = [(0, 0, 0)]
for i in range(n):
    kukan.append((kukan[i][1], kukan[i][1] + t[i] * 2, v[i]))
kukan.append((T, T, 0))
vt = [[1000] * (len(kukan)) for _ in range(T + 1)]
k = 0
for ts, te, v_ in kukan:
    for i in range(ts, te + 1):
        vt[i][k] = v_
    for i in range(ts - 1, -1, -1):
        vt[i][k] = vt[i + 1][k] + 0.5
    for i in range(te + 1, T + 1):
        vt[i][k] = vt[i - 1][k] + 0.5
    k += 1
ans = 0
d = [0] * len(vt)
for i in range(len(vt)):
    d[i] = min(vt[i])
for i in range(1, len(vt)):
    ans += (d[i] + d[i - 1]) * 0.25
print(ans)
