class Combination:
    """階乗とその逆元のテーブルをO(N)で事前作成し、組み合わせの計算をO(1)で行う"""
    def __init__(self, n, MOD):
        self.fact = [1]
        for i in range(1, n + 1):
            self.fact.append(self.fact[-1] * i % MOD)
        self.inv_fact = [0] * (n + 1)
        self.inv_fact[n] = pow(self.fact[n], MOD - 2, MOD)
        for i in reversed(range(n)):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % MOD
        self.MOD = MOD

    def factorial(self, k):
        """k!を求める O(1)"""
        return self.fact[k]

    def inverse_factorial(self, k):
        """k!の逆元を求める O(1)"""
        return self.inv_fact[k]

    def permutation(self, k, r):
        """kPrを求める O(1)"""
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r]) % self.MOD

    def combination(self, k, r):
        """kCrを求める O(1)"""
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r] * self.inv_fact[r]) % self.MOD

      
n, k = map(int, input().split())
MOD = 998244353 
comb = Combination(10 ** 6, MOD)

ball = n
box = n - k

if box <= 0:
    print(0)
    return
ans = 0
for i in range(box + 1):
    ans += pow(-1, i, MOD) * comb.combination(box, i) * pow(box - i, ball, MOD)
    ans %= MOD

if k == 0:
    print(ans * comb.combination(n, box) % MOD)
else:
    print(ans * comb.combination(n, box) * 2 % MOD)
