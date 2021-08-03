n, x = map(int, input().split())
A = list(map(int, input().split()))
d = dict()
for j in range(n):
    if A[j] in d:
        d[A[j]] += 1
    else:
        d[A[j]] = 1
ans = 0
for j in range(n):
    per = x ^ A[j]
    if A[j] != per:
        if per in d:
            ans += d[per]
    else:
        if per in d:
            ans += d[per] - 1
print(ans // 2)
