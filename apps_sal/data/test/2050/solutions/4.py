(a, b) = list(map(int, input().split(' ')))
print((6 * a - 1) * b)
for i in range(a):
    print((6 * i + 1) * b, (6 * i + 2) * b, (6 * i + 3) * b, (6 * i + 5) * b)
