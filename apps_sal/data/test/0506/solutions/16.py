

def main():
    [a, b] = list(map(int, input().split()))
    ans = 0

    while 1:
        if a > b:
            ans += a // b
            if a % b == 0:
                break
            a = a % b
        else:
            ans += b // a
            if b % a == 0:
                break
            b = b % a

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
