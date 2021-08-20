def R():
    return list(map(int, input().split()))


n = R()
a = tuple(R())
s0 = sum(a) / 2
s = 0
for i in range(len(a)):
    s += a[i]
    if s >= s0:
        print(i + 1)
        break
