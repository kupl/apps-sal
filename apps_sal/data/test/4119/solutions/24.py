n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
d = []
if n >= m:
    print((0))

else:
    x.sort()
    for i in range(m - 1):
        d.append(abs(x[i] - x[i + 1]))
    d.sort()
    print((sum(d[:m - n])))
