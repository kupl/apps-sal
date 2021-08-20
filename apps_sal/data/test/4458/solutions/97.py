def main():
    n = int(input())
    p = [int(v) for v in input().split()]
    ans = 1
    sofar = p[0]
    for i in p:
        if i < sofar:
            ans += 1
            sofar = i
    return ans


def __starting_point():
    print(main())


__starting_point()
