def main():
    x, y, z = list(map(int, input().split()))
    x -= y + z * 2
    ans = 0
    if x < 0:
        print(ans)
    while x >= 0:
        ans += 1
        x -= y + z
    print(ans)


def __starting_point():
    main()


__starting_point()
