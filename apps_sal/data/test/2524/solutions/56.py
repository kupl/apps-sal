def XorSum4():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0

    for i in range(60):
        count = 0
        for j in a:
            count += (j >> i) & 1
        num = (count * (n - count)) % mod
        ans += num * 2**i
        ans %= mod
    print(ans)


def __starting_point():
    XorSum4()


__starting_point()
