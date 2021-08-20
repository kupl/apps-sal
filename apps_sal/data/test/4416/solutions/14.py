(n, k) = list(map(int, input().split()))
(a, m, b) = ([], [], [])
for i in range(n):
    (ti, ai, bi) = list(map(int, input().split()))
    if ai == 1 and bi == 1:
        m.append(ti)
    elif ai == 1:
        a.append(ti)
    elif bi == 1:
        b.append(ti)
a.sort()
m.sort()
b.sort()
pm = [0] * (len(m) + 1)
for i in range(1, len(m) + 1):
    pm[i] = pm[i - 1] + m[i - 1]
pa = [0] * (len(a) + 1)
for i in range(1, len(a) + 1):
    pa[i] = pa[i - 1] + a[i - 1]
pb = [0] * (len(b) + 1)
for i in range(1, len(b) + 1):
    pb[i] = pb[i - 1] + b[i - 1]
ans = 10 ** 12
for c in range(min(k + 1, len(m) + 1)):
    if min(len(a), len(b)) >= k - c and ans > pm[c] + pa[k - c] + pb[k - c]:
        ans = pm[c] + pa[k - c] + pb[k - c]
if ans == 10 ** 12:
    print(-1)
else:
    print(ans)
