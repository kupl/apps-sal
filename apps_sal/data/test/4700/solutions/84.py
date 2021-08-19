def main():
    (n, m) = list(map(int, input().split()))
    h = list(map(int, input().split()))
    hf = [0] * n
    for i in range(m):
        (a, b) = list(map(int, input().split()))
        if h[a - 1] > h[b - 1]:
            hf[b - 1] = 1
        elif h[a - 1] == h[b - 1]:
            hf[a - 1] = 1
            hf[b - 1] = 1
        else:
            hf[a - 1] = 1
    print(hf.count(0))


def __starting_point():
    main()


__starting_point()
