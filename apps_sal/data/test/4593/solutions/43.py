def main():
    X = int(input())
    ans = 1
    for i in range(2, X + 1):
        for j in range(2, 11):
            if i**j > X:
                break
            else:
                ans = max(ans, i**j)
    print(ans)


def __starting_point():
    main()


__starting_point()
