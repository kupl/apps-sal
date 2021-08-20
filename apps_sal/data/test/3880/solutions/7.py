def main():
    n = int(input())
    seq = list(map(int, input().split()))
    neg = [x for x in seq if x < 0]
    seq = [abs(x) for x in seq]
    ans = sum(seq)
    if n % 2 == 0 and len(neg) % 2 == 1:
        ans = ans - 2 * sorted(seq)[0]
    print(ans)


def __starting_point():
    main()


__starting_point()
