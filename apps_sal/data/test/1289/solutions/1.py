def r(): return list(map(int, input().split()))
def ri(): return int(input())


n, a, m, b = ri(), r(), ri(), r()
c = [0] * n
for e in b:
    c[e - 1] += 1
c[0] *= 2
c[-1] *= 2
d = 0
df = 0
r = max(e // 2 for e in c)
c = [e - r * 2 for e in c]
if any(c):
    for i in range(n - 1):
        de = a[i + 1] - a[i]
        d += min(c[i], c[i + 1]) * de
        df += de
    print(d + r * 2 * df)
else:
    de = a[1] - a[0]
    for i in range(1, n - 1):
        if a[i + 1] - a[i] != de:
            print(-1)
            break
    else:
        print(r * de * 2 * (n - 1) - de)
