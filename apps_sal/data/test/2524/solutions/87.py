
def resolve():
    MOD = 10 ** 9 + 7
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(60):
        p = 1 << i
        one = sum([1 for a in A if a & p])
        zero = N - one
        ans += p * one * zero
        ans %= MOD
    print(ans)


def __starting_point():
    resolve()

__starting_point()
