class Combi():
    def __init__(self, N, mod):
        self.power = [1 for _ in range(N + 1)]
        self.rev = [1 for _ in range(N + 1)]
        self.mod = mod
        for i in range(2, N + 1):
            self.power[i] = (self.power[i - 1] * i) % self.mod
        self.rev[N] = pow(self.power[N], self.mod - 2, self.mod)
        for j in range(N, 0, -1):
            self.rev[j - 1] = (self.rev[j] * j) % self.mod

    def com(self, K, R):
        if K < R:
            return 0
        else:
            return ((self.power[K]) * (self.rev[K - R]) * (self.rev[R])) % self.mod

    def pom(self, K, R):
        if K < R:
            return 0
        else:
            return (self.power[K]) * (self.rev[K - R]) % self.mod


def main():
    mod = 10**9 + 7
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    c = Combi(N, mod)
    res = 0
    for i, v in enumerate(A):
        res += c.com(i, K - 1) * v
        res -= c.com(N - 1 - i, K - 1) * v
        res %= mod
    print(res)
    return


def __starting_point():
    main()


__starting_point()
