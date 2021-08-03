def main():
    *S, = input()
    c = S.pop()
    ans = 0
    while S:
        if (nc := S.pop()) == c:
            continue
        c = nc
        ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
