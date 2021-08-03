n, w, v, u = [int(x) for x in input().split()]
slant = u / v
x, y = [int(x) for x in input().split()]

ul = dr = v * y - u * x

for _ in range(1, n):
    x, y = [int(x) for x in input().split()]

    m, p = v * y - u * x, v * y + u * x

    if m > ul:
        ul = m
    if m < dr:
        dr = m

if ul <= 0 or dr >= 0:
    print(w / u)
else:
    print(w / u - dr / (u * v))
