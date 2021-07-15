def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        tmp = n//i
        ans += i*tmp*(tmp+1)//2
    print(ans)
    return


def __starting_point():
    main()

__starting_point()
