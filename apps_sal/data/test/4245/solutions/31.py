a, b = map(int, input().split())

g = a - 1
d, r = divmod(b - 1, g)
if r == 0:
    print(d)
else:
    print(d + 1)
