h, n = map(int, input().split())
a = list(map(int, input().split()))
b = a[:]
H = h
for i in range(1, n):
    a[i] += a[i - 1]
t = 0
for i in b:
    if H > 0:
        H += i
        t += 1
    else:
        print(t)
        return
if a[-1] >= 0:
    print(-1)
    return()
else:
    r = min(a)
    m = (h + r) // abs(a[-1])
    h += (m) * (a[-1])
    t = n * (m)
    while h > 0:
        for i in b:
            if h > 0:
                h += i
                t += 1
            else:
                break
    print(t)
