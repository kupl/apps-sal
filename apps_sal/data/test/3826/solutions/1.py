n = int(input())
a = list(map(int, input().split()))
s, d = {}, {}
for q in range(n):
    s[a[q]] = q
    d[a[q]] = d.get(a[q], 0) + 1
q2, ans = 0, n - 1
for q1 in d:
    while d[q1] > 1:
        d[a[q2]] -= 1
        q2 += 1
f = set()
for q in range(n):
    ans = min(ans, q2 - q)
    if a[q] in f:
        break
    f.add(a[q])
    q2 = max(q2, s[a[q]] + 1, q + 1)
print(ans)
