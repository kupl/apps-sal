def f(n, r, p, q):
    if r < 1 or r > n:
        return 0
    if p < 1 or p > n:
        return 0
    if q < 1 or q > n:
        return 0
    return 1


(n, a, b, c, d) = [int(i) for i in input().split()]
box = 0
for i in range(1, n + 1):
    r = i + b - c
    p = r + a - d
    q = p + c - b
    box += f(n, r, p, q)
    '\n    for j in range(1, n + 1):\n        print(i, a, r)\n        print(b, j, c)\n        print(q, d, p)\n        print()\n        '
box *= n
print(box)
