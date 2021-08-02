def ans():
    N = int(input())
    Z = []  # x + y
    W = []  # x - y
    for _ in range(N):
        x, y = map(int, input().split())
        Z.append(x + y)
        W.append(x - y)

    z_max, z_min = max(Z), min(Z)
    w_max, w_min = max(W), min(W)

    max_d = max((z_max - z_min, w_max - w_min))
    print(max_d)


def __starting_point():
    ans()


__starting_point()
