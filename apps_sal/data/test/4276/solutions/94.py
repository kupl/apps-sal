
def main():
    n, time = list(map(int, input().split()))
    ans = 1001
    for i in range(n):
        c, t = list(map(int, input().split()))
        if t <= time:
            ans = min(ans, c)
    print((ans if ans != 1001 else 'TLE'))


def __starting_point():
    main()


__starting_point()
