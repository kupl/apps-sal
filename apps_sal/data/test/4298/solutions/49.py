(n, d) = map(int, input().split())
x = 2 * d + 1
if n % x == 0:
    print(n // x)
else:
    print(n // x + 1)
