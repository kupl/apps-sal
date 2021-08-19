MOD = pow(10, 9) + 7


def MODINV(n: int, MOD=MOD):
    return pow(n, MOD - 2, MOD)


class common_combinations:
    """
        mod を含む combination を高速に求める関数
        N < 5*10^6 まで対応. それ以上の N の場合は common.combi(n, k) を使用する.
        __init__: nCk を求めるための事前の計算を行う. O(N)
        combinations: nCk を求める. O(1)
    """

    def __init__(self, N=510000, MOD=pow(10, 9) + 7):
        """
            combination を O(1) で計算するための前処理
        """
        self.N = N
        self.MAX_NUM = self.N + 1
        self.MOD = MOD
        self.fac = [0 for _ in range(self.MAX_NUM)]
        self.finv = [0 for _ in range(self.MAX_NUM)]
        self.inv = [0 for _ in range(self.MAX_NUM)]
        self.fac[0] = self.fac[1] = 1
        self.finv[0] = self.finv[1] = 1
        self.inv[1] = 1
        for i in range(2, self.MAX_NUM):
            self.fac[i] = self.fac[i - 1] * i % self.MOD
            self.inv[i] = self.MOD - self.inv[self.MOD % i] * (self.MOD // i) % self.MOD
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.MOD

    def combinations(self, n: int, k: int):
        """
            combination を計算して返すメソッド
        """
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fac[n] * (self.finv[k] * self.finv[n - k] % self.MOD) % self.MOD


def main():
    (N, K) = list(map(int, input().split()))
    combi = common_combinations(N=N + 10)
    ans = 0
    for i in range(1, K + 1):
        lineup = combi.combinations(N - K + 1, i)
        block = combi.combinations(K - 1, i - 1)
        print(lineup * block % MOD)


def __starting_point():
    main()


__starting_point()
