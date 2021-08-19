def main():
    n = int(input())
    cards = list(map(int, input().split()))
    cards.sort(reverse=True)
    (alice, bob) = (0, 0)
    if n % 2 == 0:
        for i in range(int(n / 2)):
            alice += cards[2 * i]
            bob += cards[2 * i + 1]
    else:
        for j in range(int(n / 2)):
            alice += cards[2 * j]
            bob += cards[2 * j + 1]
        alice += cards[n - 1]
    ans = alice - bob
    print(ans)


def __starting_point():
    main()


__starting_point()
