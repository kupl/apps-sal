def LI(): return list(map(int, input().split()))


N = input()


def main():
    if N[0] == N[2]:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)


def __starting_point():
    main()


__starting_point()
