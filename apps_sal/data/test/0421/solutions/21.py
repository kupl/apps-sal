n = int(input())
a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
a = sorted(a, key=lambda y: (y[0], y[1] - y[0]))
prev = (0, 0)
orders = 0
for order in a:
    s, e = order
    if s > prev[1]:
        prev = order
        orders += 1
    elif e < prev[1]:
        prev = order
print(orders)
