mod = 998244353
(n, k) = map(int, input().split())
k = abs(k)


def count(num):
    if num <= n:
        return num - 1
    else:
        return num - 1 - (num - n - 1) * 2


def main():
    ans = 0
    for i in range(k + 2, 2 * n + 1):
        j = i - k
        ans += count(i) * count(j)
    print(ans)


def __starting_point():
    main()


__starting_point()
