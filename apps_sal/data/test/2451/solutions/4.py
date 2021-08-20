def main():
    (n, h, a, b, k) = [int(x) for x in input().split()]
    for _ in range(k):
        (ta, fa, tb, fb) = [int(x) for x in input().split()]
        if ta == tb:
            print(abs(fa - fb))
            continue
        sum = 0
        if not a <= fa <= b:
            if fa < a:
                sum += a - fa
                sum += abs(a - fb)
            else:
                sum += fa - b
                sum += abs(b - fb)
        else:
            sum = abs(fa - fb)
        print(abs(ta - tb) + sum)


def __starting_point():
    main()


__starting_point()
