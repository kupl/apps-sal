n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
s = [0] * (2 * m + 1)
cnt = [0] * (m + 1)
for i in range(n - 1):
    cnt[a[i + 1]] += (a[i + 1] + m - a[i]) % m - 1
for i in range(n - 1):
    s[a[i] + 1] += 1
    if a[i + 1] < a[i]:
        s[a[i + 1] + m] -= 1
    else:
        s[a[i + 1]] -= 1

for i in range(2 * m):
    s[i + 1] += s[i]
for i in range(1, m + 1):
    s[i] = s[i] + s[i + m]

tmp = 0
for i in range(n - 1):
    if a[i + 1] < a[i]:
        tmp += (a[i + 1] - 1) + 1
    else:
        tmp += (a[i + 1] - a[i])
ans = tmp
for i in range(2, m + 1):
    tmp = tmp + cnt[i - 1] - s[i - 1]
    ans = min(ans, tmp)
print(ans)

