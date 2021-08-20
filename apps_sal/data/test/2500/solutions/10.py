N = int(input())
(a, b, c) = (1, 0, 0)
for i in range(80)[::-1]:
    if N >> i & 1:
        (a, b, c) = (a, a + b, 2 * b + 3 * c)
    else:
        (a, b, c) = (a + b, b, b + 3 * c)
print((a + b + c) % (10 ** 9 + 7))
