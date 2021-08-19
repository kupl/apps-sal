(N, M, K) = map(int, input().split())
MOD = 998244353
fact = [0] * (N + 1)
inv = [0] * (N + 1)
fact[0] = fact[1] = 1
inv[1] = 1
for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD


def main():
    if N == 1:
        print(M)
        return
    num = M
    nums = [M]
    for i in reversed(range(1, N)):
        num *= i * (M - 1)
        num *= inv[N - i]
        num %= MOD
        nums.append(num)
    nums.reverse()
    print(sum(nums[:K + 1]) % MOD)


def __starting_point():
    main()


__starting_point()
