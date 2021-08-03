def divide_into_three(X, Y):
    minimum = float("inf")
    for x in range(1, X):
        b1 = x * Y
        if not all(((X - x) & 1, Y & 1)):
            b2 = b3 = ((X - x) * Y) >> 1
        else:
            s, l = sorted((X - x, Y))
            b2 = s * (l >> 1)
            b3 = s * l - b2
        diff = max((b1, b2, b3)) - min((b1, b2, b3))
        minimum = min(minimum, diff)
    return minimum


H, W = map(int, input().split())
print(min(divide_into_three(H, W), divide_into_three(W, H)))
