def solve(a, b, x, y, n):
    x = a - x
    y = b - y
    m = min(x, n)
    n -= m
    a -= m
    m = min(y, n)
    b -= m
    return a * b


for _ in range(int(input())):
    a, b, x, y, n = list(map(int, input().split()))
    print(min(solve(a, b, x, y, n), solve(b, a, y, x, n)))
