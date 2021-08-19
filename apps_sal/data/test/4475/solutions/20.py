t = int(input())
for _ in range(t):
    (a, b, x, y, n) = list(map(int, input().split()))
    min_a = max(a - n, x)
    min_b = max(b - n, y)
    if min_a < min_b:
        n = n - (a - min_a)
        a = min_a
        b = max(b - n, y)
    else:
        n = n - (b - min_b)
        b = min_b
        a = max(a - n, x)
    print(a * b)
