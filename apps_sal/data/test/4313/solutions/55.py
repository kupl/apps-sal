import itertools
n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
xy = 0
for i in range(1, n + 1):
    for h in itertools.combinations(range(0, n), i):
        x = 0
        y = 0
        for j in h:
            x += v[j]
            y += c[j]
        if xy < x - y:
            xy = x - y
print(xy)
