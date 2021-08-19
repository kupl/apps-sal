def abc121_d():
    (a, b) = map(int, input().split())
    ans = 0
    if b - a < 8:
        for k in range(a, b + 1):
            ans ^= k
    else:
        low = (a + 3) // 4
        up = b // 4
        for k in range(a, 4 * low):
            ans ^= k
        for k in range(4 * up, b + 1):
            ans ^= k
    print(ans)


def __starting_point():
    abc121_d()


__starting_point()
