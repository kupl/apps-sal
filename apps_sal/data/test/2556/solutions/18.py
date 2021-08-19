def main():

    def solve():
        (c, sum) = map(int, input().split())
        pan = sum // c
        extra = sum % c
        result = (c - extra) * pan * pan + extra * (pan + 1) * (pan + 1)
        print(result)
    q = int(input())
    for _ in range(q):
        solve()


def __starting_point():
    main()


__starting_point()
