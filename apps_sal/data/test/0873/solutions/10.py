def main():
    n = int(input())
    b = input()
    a = input()
    ans = 0
    for i in range(n):
        ans += min(abs(int(b[i]) - int(a[i])), 10 - abs(int(b[i]) - int(a[i])))
    print(ans)


def __starting_point():
    main()


__starting_point()
