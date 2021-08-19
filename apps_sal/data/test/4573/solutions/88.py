def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = [0] * n
    x_sort = sorted(x)
    a = x_sort[1:n]
    a_med = a[n // 2 - 1]
    b = x_sort[0:n - 1]
    b_med = b[n // 2 - 1]
    for i in range(n):
        if x[i] < a_med:
            ans[i] = a_med
        else:
            ans[i] = b_med
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
