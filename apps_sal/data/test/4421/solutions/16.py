n, k = map(int, input().split())
a = list(map(int, input().split()))
d = dict()
for i in range(n):
    m = a[i] % k
    if m not in d:
        d[m] = 1
    else:
        d[m] += 1
ans = 0
if 0 in d:
    ans = d[0] // 2
h = k // 2
if k % 2 == 0 and h in d:
    ans += d[h] // 2
for i in range(1, (k + 1) // 2):
    if i in d and k - i in d:
        ans += min(d[i], d[k - i])
print(ans * 2)
