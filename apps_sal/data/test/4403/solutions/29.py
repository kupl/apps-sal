
def main():
    s = input()
    ans = 0

    for i in range(4):
        if s[i] == '+':
            ans += 1
        elif s[i] == '-':
            ans -= 1

    print(ans)


def __starting_point():
    main()


__starting_point()
