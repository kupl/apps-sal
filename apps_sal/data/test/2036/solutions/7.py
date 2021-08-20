(n, m, Sx, Sy) = (int(i) for i in input().split())
print(Sx, Sy)
for x in range(1, n + 1):
    if x == Sx:
        continue
    print(x, Sy)
for y in range(1, m + 1):
    if y == Sy:
        continue
    if x == 1:
        for x in range(1, n + 1):
            print(x, y)
    elif x == n:
        for x in reversed(range(1, n + 1)):
            print(x, y)
    else:
        assert False
