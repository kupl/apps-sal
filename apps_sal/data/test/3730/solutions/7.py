def main():
    n = int(input())
    a = [10 ** 10] + list(map(int, input().split())) + [-10 ** 10]
    if n == 1:
        print(1)
        return
    b = [0] * (n + 10)
    c = [0] * (n + 10)
    i = 1
    while i <= n:
        for j in range(i, n + 1):
            if a[j] >= a[j + 1]:
                break
        for k in range(i, j + 1):
            b[k] = i
            c[k] = j
        i = j + 1
    ans = max(c[2], n - b[n - 1] + 1, c[1], n - b[n] + 1)
    for i in range(2, n):
        ans = max(ans, c[i] - i + 2, i - b[i] + 2)
        if a[i - 1] + 1 < a[i + 1]:
            ans = max(ans, c[i + 1] - b[i - 1] + 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
