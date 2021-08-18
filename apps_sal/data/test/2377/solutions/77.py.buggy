from math import ceil
n, h = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
dmax = max(a)
b.sort(reverse=True)
ans = 0
for d in b:
    if h <= 0:
        print(ans)
        return
    if d < dmax:
        break
    h -= d
    ans += 1
if h <= 0:
    print(ans)
    return
print(ans + ceil(h / dmax))
