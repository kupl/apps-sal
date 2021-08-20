(a, b, c) = [int(x) for x in input().split()]
if a == b:
    print(a + 2 * c + b)
else:
    print(2 * min(a, b) + 1 + 2 * c)
