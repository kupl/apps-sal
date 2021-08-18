n, m = map(int, input().split())
x, k, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * m
j = 0
for i in range(n):
    if j == m:
        break
    if a[i] == b[j]:
        c[j] = i + 1
        j += 1
if not j == m:
    print(-1)
    return
a.insert(0, 0)
a.append(0)
c.insert(0, 0)
c.append(n + 1)
ans = 0
for i in range(m + 1):
    if c[i + 1] - c[i] == 1:
        continue
    l = c[i + 1] - c[i] - 1
    s = 0
    t = max(a[c[i]], a[c[i + 1]])
    for j in range(c[i] + 1, c[i + 1]):
        if a[j] > t:
            s += 1
    if s == 0:
        ans += min(l * y, (l // k) * x + (l % k) * y)
    else:
        if k > l:
            print(-1)
            return
        ans += min((l - k) * y + x, (l // k) * x + (l % k) * y)
print(ans)
