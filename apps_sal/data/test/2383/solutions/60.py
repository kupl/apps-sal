def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 1
    ans = 0
    for i in range(n):
        if a[i] != s:
            ans += 1
        else:
            s += 1
    if ans == n:
        print((-1))
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
