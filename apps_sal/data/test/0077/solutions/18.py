n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
s = 0
for i in range(n):
    if a[i] > 0:
        s += a[i]
    else:
        break
if s % 2:
    print(s)
else:
    mx = -100000
    for i in range(n):
        if a[i] < 0 and a[i] % 2:
            mx = max(a[i], mx)
    mn = 100000
    for i in range(n):
        if a[i] >= 0 and a[i] % 2:
            mn = min(a[i], mn)
    print(max(s + mx, s - mn))
