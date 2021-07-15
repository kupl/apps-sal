# coding: utf-8


def main():
    A, B, C, X, Y = list(map(int, input().split()))
    ans = 0
    min_p = min(X, Y)
    d = X - Y

    if A + B > 2 * C:
        ans += 2 * C * min_p
    else:
        ans += (A + B) * min_p

    if d > 0:
        if A > 2 * C:
            ans += 2 * C * d
        else:
            ans += A * d
    elif d < 0:
        if B > 2 * C:
            ans += 2 * C * -d
        else:
            ans += B * -d

    print(ans)

def __starting_point():
    main()

__starting_point()
