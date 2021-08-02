x, n = map(int, input().split())
p = [int(s) for s in input().split()]
for i in range(x + 1):
    for j in range(-1, +2):
        a = x + i * j
        if p.count(a) == 0:
            print(a)
            return
