def main():
    d, k, a, b, t = list(map(int, input().split()))
    res = [d * b]
    if d // k:
        x = d // k * (a * k + t)
        res.append(x + d % k * a)
        res.append(x - t + d % k * b)
        res.append(k * a + (d - k) * b)
    else:
        res.append(d * a)
    print(min(res))


def __starting_point():
    main()


__starting_point()
