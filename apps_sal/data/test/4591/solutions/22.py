def slove():
    (A, B, C, X, Y) = map(int, input().split())
    '\n    possible combinations are below.\n        A * x + B * y   \n        if x < y: B * abs(x-y) + C * min(x,y) * 2\n        if x > y: A * abs(x-y) + C * min(x,y) * 2\n        C * max(x,y) * 2\n    '
    ans1 = A * X + B * Y
    if X < Y:
        ans2 = B * abs(X - Y) + C * 2 * min(X, Y)
    else:
        ans2 = A * abs(X - Y) + C * 2 * min(X, Y)
    ans3 = C * 2 * max(X, Y)
    print(min(ans1, ans2, ans3))


def __starting_point():
    slove()


__starting_point()
