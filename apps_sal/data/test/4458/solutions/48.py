def main():
    _ = int(input())
    P = [int(x) for x in input().split()]
    res = P[0]
    ans = 0
    for p in P:
        if p <= res:
            ans += 1
            res = p
    print(ans)


def __starting_point():
    main()


__starting_point()
