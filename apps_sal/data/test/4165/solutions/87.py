def main():
    input()
    l = list(map(int, input().split()))
    m = max(l)
    s = sum(l) - m
    ans = 'Yes' if m < s else 'No'
    print(ans)


def __starting_point():
    main()


__starting_point()
