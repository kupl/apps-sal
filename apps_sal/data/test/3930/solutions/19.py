(n, k) = map(int, input().split())
powk = [k ** i for i in range(1, 60)]
a = list(map(int, input().split()))
s = 0
d = {0: 1}
ans = 0
INF = 10 ** 14
for i in range(n):
    s += a[i]
    if s - 1 in d:
        ans += d[s - 1]
    for j in range(len(powk)):
        q = powk[j]
        if q == 1:
            break
        if s - q in d:
            ans += d[s - q]
        if abs(j) > INF:
            break
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
print(ans)
