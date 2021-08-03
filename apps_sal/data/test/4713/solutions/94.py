def main():
    input()
    s = input()
    tmp = 0
    ans = 0
    for v in s:
        if v == "I":
            tmp += 1
        else:
            tmp -= 1
        ans = max(ans, tmp)
    print(ans)


def __starting_point():
    main()


__starting_point()
