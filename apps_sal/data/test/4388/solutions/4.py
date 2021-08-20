def main():
    N = input()
    ans = ''
    for n in N:
        if n == '1':
            ans += '9'
        else:
            ans += '1'
    print(ans)


def __starting_point():
    main()


__starting_point()
