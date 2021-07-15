n, k = map(int, input().split())
v = list(map(int, input().split()))
vv = [0] * (n + 1)
for i in range(n):
    vv[i + 1] = vv[i] + v[i]
sumv = vv[n]
ans = 0
for l in range(n):
    for r in range(l - 1, n):
        c = r - l + 1
        if n - c > k:
            continue
        x = []
        value = sumv - (vv[r + 1] - vv[l])
        for i in range(n):
            if not l <= i <= r:
                x.append(v[i])
        x.sort()
        for i in range(max(0, min(k - (n - c), len(x)))):
            if x[i] < 0:
                value -= x[i]
            else:
                break
        ans = max(value, ans)
print(ans)
