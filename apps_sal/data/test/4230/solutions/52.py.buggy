x, n = map(int, input().split())
try:
    p = sorted([*map(int, input().split())])
except:
    print(x)
    return
for i in range(x + 1):
    for s in [-1, 1]:
        a = x + i * s
        if p.count(a) == 0:
            print(a)
            return
