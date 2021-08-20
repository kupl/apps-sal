for _ in range(int(input())):
    (a, b, x, y) = map(int, input().split())
    w = max(a - 1 - x, x)
    h = max(b - 1 - y, y)
    ans = max(w * b, h * a)
    print(ans)
