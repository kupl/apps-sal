def main():
    x = int(input())
    div = x//11
    rem = x%11
    ans = div*2 + (1 <= rem <= 10) + (7 <= rem <= 10)
    print(ans)


def __starting_point():
    main()

__starting_point()
