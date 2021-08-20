def main():
    n = int(input())
    a = list(map(int, input().split()))
    im = 1
    while im < n and a[im] >= a[im - 1]:
        im += 1
    if sorted(a[im:] + a[:im]) == a[im:] + a[:im]:
        print(n - im)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
