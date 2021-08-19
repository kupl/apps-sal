(x, y, k) = [int(i) for i in input().split()]
o = 0
for i in range(k):
    o += x * 2 + (y - 2) * 2
    y -= 4
    x -= 4
print(o)
