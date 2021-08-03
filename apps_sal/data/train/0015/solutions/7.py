t = int(input())
for _ in range(t):
    a, b, x, y = map(int, input().split())

    l = max(a * y, a * (b - y - 1))
    ll = max(b * x, b * (a - x - 1))
    print(max(l, ll))
