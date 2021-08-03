n = int(input())
x = int(n ** 0.5)
y = n // x

if x * y != n:
    print(2 * (x + y) + 2)
else:
    print(2 * (x + y))
