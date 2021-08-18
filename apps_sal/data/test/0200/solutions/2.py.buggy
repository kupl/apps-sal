from math import ceil

h1, h2 = list(map(int, input().split()))

a, b = list(map(int, input().split()))

x = h2 - h1
p = 0

for i in range(8):
    p += a
    if p >= x:
        print(0)
        return

for i in range(100000):
    for j in range(12):
        if i & 1:
            p += a
        else:
            p -= b
        if p >= x:
            print(ceil(i / 2))
            return

print(-1)
