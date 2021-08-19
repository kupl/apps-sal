(f, d, s) = (0, 0, 0)
(a, b) = map(int, input().split())
for i in range(1, 7):
    if abs(a - i) == abs(b - i):
        d += 1
    elif abs(a - i) < abs(b - i):
        f += 1
    else:
        s += 1
print(f, d, s)
