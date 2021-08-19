(N, x) = map(int, input().split())
a = list(map(int, input().split()))
r1 = sum(a)
flow = 0
for i in range(1, N):
    t = a[i] + a[i - 1] - x
    if flow != 0:
        a[i - 1] -= flow
        t -= flow
        flow = 0
    if t > 0:
        if t > a[i]:
            t -= a[i]
            a[i - 1] -= t
            t = a[i]
        flow = t
a[-1] -= flow
r2 = sum(a)
print(r1 - r2)
