def main():
    n, m, k = list(map(int, input().split()))
    m -= k
    if m > 0:
        for i, a in enumerate(sorted(map(int, input().split()), reverse=True), 1):
            m -= a - 1
            if m <= 0:
                print(i)
                break
        else:
            print(-1)
    else:
        print(0)


def __starting_point():
    main()

__starting_point()
