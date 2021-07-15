def main():
    p, q, l, r = list(map(int, input().split()))
    Z = set()
    X = []

    for _ in range(p):
        ai, bi = list(map(int, input().split()))
        Z.update(list(range(ai, bi+1)))
    for _ in range(q):
        ai, bi = list(map(int, input().split()))
        X.extend(list(range(ai, bi+1)))

    res = 0
    for i in range(l, r+1):
        for j in X:
            if j + i in Z:
                res += 1
                break
    print(res)


def __starting_point():
    main()


__starting_point()
