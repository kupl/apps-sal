def actions(n, k, h):
    j = 0

    smin = sum([h[x] for x in range(0, k)])
    last = smin

    for i in range(1, n - k + 1):
        s = last - h[i - 1] + h[i + k - 1]
        last = s
        if s < smin:
            smin = s
            j = i

    return j + 1


def main():
    n, k = list(map(int, input().split()))
    h = list(map(int, input().split()))

    print(actions(n, k, h))


def __starting_point(): main()


__starting_point()
