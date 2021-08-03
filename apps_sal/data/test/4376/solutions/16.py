def R(): return list(map(int, input().split()))


n, m = R()
a = list(R())
a.append(10**6)

s = 0
f = 0

for b in R():
    while s < b:
        s += a[f]
        f += 1
    print(f, b - s + a[f - 1])
