def main():
    p, q, l, r = map(int, input().split())
    ab, cd = [False] * 1001, [False] * 1001
    for _ in range(p):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            ab[i] = True
    for _ in range(q):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            cd[i] = True
    res = 0
    for i in range(l, r + 1):
        for t, f in enumerate(ab):
            if f and cd[t - i] and t >= i:
                res += 1
                break
    print(res)


def __starting_point():
    main()
__starting_point()
