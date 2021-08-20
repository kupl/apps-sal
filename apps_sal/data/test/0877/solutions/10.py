(n, m) = map(int, input().split())
a = [0] * (n + 1)
c = [0] * 4
d = [0] * 4
ans = 0
for i in range(m):
    (x, y) = sorted(map(int, input().split()))
    a[x] |= 1
    a[y] |= 2
for x in a:
    c[x] += 1
if c[3] == 0:
    for i in range(1, n):
        if a[i] > 1:
            break
        d[a[i]] += 1
        c[a[i]] -= 1
        if c[1] > 0:
            continue
        ans += 1
print(ans)
