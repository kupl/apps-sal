3

MOD = 998244353

def solve(N, A):
    ans = 0

    k = 1
    ans += k * A[-1]
    ans %= MOD

    for i in range(N - 2, -1, -1):
        ans += k * (N + 1 - i) * A[i]
        ans %= MOD
        k *= 2
        k %= MOD

    return ans


def main():
    N = int(input())
    A = [int(e) for e in input().split(' ')]
    assert len(A) == N
    print(solve(N, A))


def __starting_point():
    main()

__starting_point()
