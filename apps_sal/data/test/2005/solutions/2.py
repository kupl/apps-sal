def main():
    n, n1, n2 = list(map(int, input().split()))
    if n1 > n2:
        n1, n2 = n2, n1
    aa = sorted(map(int, input().split()), reverse=True)
    print(sum(aa[:n1]) / n1 + sum(aa[n1:n1 + n2]) / n2)


def __starting_point():
    main()

__starting_point()
