class Combi:

    def __init__(self, N, mod):
        self.power = [1 for _ in range(N + 1)]
        self.rev = [1 for _ in range(N + 1)]
        self.mod = mod
        for i in range(2, N + 1):
            self.power[i] = self.power[i - 1] * i % self.mod
        self.rev[N] = pow(self.power[N], self.mod - 2, self.mod)
        for j in range(N, 0, -1):
            self.rev[j - 1] = self.rev[j] * j % self.mod

    def com(self, K, R):
        if K < R:
            return 0
        else:
            return self.power[K] * self.rev[K - R] * self.rev[R] % self.mod

    def pom(self, K, R):
        if K < R:
            return 0
        else:
            return self.power[K] * self.rev[K - R] % self.mod


def main():
    (N, M) = map(int, input().split())
    mod = 10 ** 9 + 7
    c = Combi(5 * 10 ** 5, mod)
    ans = c.pom(M, N) ** 2 % mod
    for k in range(1, N + 1):
        s = (-1) ** ((k - 1) % 2)
        t = c.com(N, k)
        u = c.pom(M - k, N - k) ** 2
        v = c.pom(M, k)
        ans -= s * t * u * v
        ans = ans % mod
    print(ans)


def __starting_point():
    main()


__starting_point()
