
def solve(N, As):
    import math
    x = 1 if max(As) == 0 else math.ceil(math.log2(max(As)))
    ans = 0
    mod = 10 ** 9 + 7

    for i in range(x):
        cnt = sum((A >> i) % 2 for A in As)
        ans += (cnt * (N - cnt)) * pow(2, i, mod)
        ans = ans % mod
    print(ans)


def __starting_point():
    N = int(input())
    As = [int(i) for i in input().split()]
    solve(N, As)


__starting_point()
