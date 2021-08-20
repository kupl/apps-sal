def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        for i in range(1, 31):
            if a % 2 ** i != 0:
                ans += i - 1
                break
    print(ans)


def __starting_point():
    main()


__starting_point()
