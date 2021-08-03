def main():
    n = int(input())
    ans = 0
    for v in range(1, n + 1):
        if len(str(v)) % 2 == 1:
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
