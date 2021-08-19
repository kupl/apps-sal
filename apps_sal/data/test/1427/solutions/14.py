from collections import defaultdict
import sys
input = sys.stdin.readline


class PrimeFactor():

    def __init__(self, n):                  # エラトステネス　O(N loglog N)
        self.n = n
        self.table = [i if i % 2 else 2 for i in range(n + 1)]
        self.table[0] = 0
        for p in range(3, n + 1):
            if self.table[p] == p:
                for q in range(p * p, n + 1, 2 * p):
                    self.table[q] = p

    def is_prime(self, x):  # 素数判定　O(1)
        if x < 2:
            return False
        return self.table[x] == x

    def prime_factors(self, x):             # 素因数分解 O(logN)
        res = []
        if x < 2:
            return res
        while self.table[x] != 1:
            res.append(self.table[x])
            x //= self.table[x]
        return res

    def prime_counter(self, x):             # 素因数分解（個数のリスト）
        res = defaultdict(int)
        if x < 2:
            return res
        while self.table[x] != 1:
            res[self.table[x]] += 1
            x //= self.table[x]
        return res

    def prime_gcd(self, X):                 # n個の最大公約数　X:n個のリスト
        exponents = self.prime_counter(X[0])
        for x in X[1:]:
            Y = self.prime_counter(x)
            for prime, exp in exponents.items():
                if Y[prime] < exp:
                    exponents[prime] = Y[prime]
        res = 1
        for prime, exp in exponents.items():
            res *= pow(prime, exp)
        return res

    def prime_lcm(self, X, mod=None):       # n個の最小公倍数　X:n個のリスト
        exponents = defaultdict(int)
        for x in X:
            for prime, exp in self.prime_counter(x).items():
                if exp > exponents[prime]:
                    exponents[prime] = exp
        res = 1
        for prime, exp in exponents.items():
            res *= pow(prime, exp, mod)
        if mod == None:
            return res
        else:
            return res % mod


mod = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))
table = PrimeFactor(10**6)
num = table.prime_lcm(A, mod)

res = 0
for a in A:
    res += num * pow(a, mod - 2, mod)

print(res % mod)
