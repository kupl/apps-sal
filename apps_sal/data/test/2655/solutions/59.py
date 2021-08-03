
def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = a[0]
    t = N - 2

    for i in range(1, N):
        for _ in range(2):
            if t > 0:
                ans += a[i]
                t -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
