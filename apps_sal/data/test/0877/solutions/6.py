n, m = map(int, input().split())
a = list(0 for i in range(n))
e = 0
if m == 0:
    print(n - 1)
    return
for i in range(m):
    q, w = map(int, input().split())
    if a[min(q, w) - 1] == 0:
        a[min(q, w) - 1] = 1
    if a[min(q, w) - 1] == 2:
        e = 1
        break
    if a[max(q, w) - 1] == 0:
        a[max(q, w) - 1] = 2
    if a[max(q, w) - 1] == 1:
        e = 1
        break
c = r = t = 0
if e == 1:
    print(0)
else:
    for i in range(n):
        if a[i] == 1:
            r = i
    for i in range(n):
        if a[i] == 2:
            t = i
            break
    print(t - r if t > r else 0)
