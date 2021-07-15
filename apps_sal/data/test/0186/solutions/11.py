n, m = map(int, input().split())
a, b = 2 * n, 3 * m
for i in range(6, 10 ** 10, 6):
    if a >= i and b >= i:
        if a <= b:
            a += 2
        else:
            b += 3
    else:
        break
print(max(a, b))
