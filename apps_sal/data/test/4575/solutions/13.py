(n, d, x, *a) = map(int, open(0).read().split())
for i in a:
    x += 1 + (d - 1) // i
print(x)
