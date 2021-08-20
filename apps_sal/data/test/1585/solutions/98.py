def main():
    (X, Y) = map(int, input().split())
    ans = 1
    x = X
    for i in range(Y):
        if x * 2 > Y:
            break
        else:
            x *= 2
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
