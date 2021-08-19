(a, b) = list(map(int, input().strip().split(' ')))
while True:
    if a == 0 or b == 0:
        break
    if a >= 2 * b:
        d = a // (2 * b)
        d = max(d - 1, 1)
        a = a - d * 2 * b
    if a == 0 or b == 0:
        break
    if b >= 2 * a:
        d = b // (a * 2)
        d = max(d - 1, 1)
        b = b - d * 2 * a
    if a == 0 or b == 0:
        break
    if a < 2 * b and b < 2 * a:
        break
print(a, b)
