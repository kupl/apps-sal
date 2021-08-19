for i in range(int(input())):
    (x, y) = map(int, input().split())
    (a, b) = map(int, input().split())
    b = min(2 * a, b)
    mi = min(x, y)
    ma = max(x, y)
    ans = mi * b + (ma - mi) * a
    print(ans)
