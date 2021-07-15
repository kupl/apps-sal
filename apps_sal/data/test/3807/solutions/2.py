def main():
    def f(n):
        if n < 8:
            return [n, n]
        a = int((n + .5) ** 0.3333333333333333)
        r1 = f(n - a * a * a)
        r1[1] += a * a * a
        a -= 1
        r2 = f(3 * a * (a + 1))
        r2[1] += a * a * a
        if r1 < r2:
            r1 = r2
        r1[0] += 1
        return r1

    print(*f(int(input())))


def __starting_point():
    main()

__starting_point()
