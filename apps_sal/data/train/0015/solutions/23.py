t = int(input())
for _ in range(t):
    (a, b, x, y) = list(map(int, input().split()))
    h = max(a - x - 1, x) * b
    v = max(b - y - 1, y) * a
    print(max(h, v))
