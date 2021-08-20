(N, K) = map(int, input().split())
x = 1
c = [0]
for s in input():
    if int(s) == x:
        c[-1] += 1
    else:
        x ^= 1
        c.append(1)
if not x:
    c.append(0)
m = len(c)
h = min(K * 2 + 1, m)
r = [c[0]]
for i in range(1, m):
    r.append(r[-1] + c[i])
r.append(0)
ans = 0
for i in range(0, m - h + 1, 2):
    ans = max(r[i + h - 1] - r[i - 1], ans)
print(ans)
