class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        self.primes = [2, 3, 5, 7, 11]
        self.get_primes(N)
        self.get_factors(2 * N)
        ans = 0
        for factor in self.factor_arr:
            x = ((2 * N) / factor - factor - 1) / 2
            if x < 0:
                continue
            if x % 1 == 0:
                ans += 1
        return ans

    def get_factors(self, n):
        self.factors = {1: 1}
        self.factor_arr = [1]
        i = 0
        while(n > 1 and i < len(self.primes)):
            prime = self.primes[i]
            pw = 0
            while(n % prime == 0):
                n = n / prime
                pw += 1
            while(pw):
                length = len(self.factor_arr)
                for fi in range(length):
                    nf = self.factor_arr[fi] * prime
                    if nf not in self.factors:
                        self.factors[nf] = 1
                        self.factor_arr += [nf]
                pw -= 1
            i += 1
        if n > 1:
            length = len(self.factor_arr)
            for i in range(length):
                nf = self.factor_arr[i] * n
                if nf not in self.factors:
                    self.factors[nf] = 1
                    self.factor_arr += [nf]
        return

    def get_primes(self, n):
        last_prime = self.primes[-1]
        k = last_prime // 6
        adds = [1, 5]
        i = adds.index(last_prime % 6)
        i += 1
        if i == 2:
            k += 1
            i = 0
        num = 6 * k + adds[i]

        while(num * num < n):
            if self.is_prime(num):
                self.primes += [num]
            i = i + 1
            if i == 2:
                k += 1
                i = 0
            num = 6 * k + adds[i]

    def is_prime(self, n):
        for prime in self.primes:
            if prime * prime > n:
                break
            if n % prime == 0:
                return False
        return True
