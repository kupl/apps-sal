def slove():
    A, B, C, X, Y = map(int, input().split())
    """
    possible combinations are below.
        A * x + B * y   
        if x < y: B * abs(x-y) + C * min(x,y) * 2
        if x > y: A * abs(x-y) + C * min(x,y) * 2
        C * max(x,y) * 2
    """
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
