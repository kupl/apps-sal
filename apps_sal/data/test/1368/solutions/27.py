def main():
    from decimal import Decimal

    N, A, B = list(map(int, input().split()))
    *v, = list(map(Decimal, input().split()))

    v.sort(reverse=True)

    max_average = sum(v[:A]) / A

    tail = v[A - 1]
    contained = [0] * (N + 1)
    s = 0
    for i, x in enumerate(v, start=1):
        if x == tail:
            s += 1
        contained[i] = s

    def choose(n, a):
        x, y = 1, 1
        for i in range(a):
            x = x * (n - i)
            y = y * (i + 1)
        return x // y

    count = 0
    for k in range(A, B + 1):
        if (k > A) and (v[k - 1] != max_average): break
        count += choose(contained[-1], contained[k])

    print(max_average)
    print(count)


def __starting_point():
    main()


__starting_point()
