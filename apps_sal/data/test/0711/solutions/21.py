import sys
import math


def main():
    mod = 1000000007
    inf = float('inf')
    sys.setrecursionlimit(10 ** 6)

    def input():
        return sys.stdin.readline().rstrip()

    def ii():
        return int(input())

    def mi():
        return list(map(int, input().split()))

    def mi_0():
        return [int(x) - 1 for x in input().split()]

    def lmi():
        return list(map(int, input().split()))

    def lmi_0():
        return list([int(x) - 1 for x in input().split()])

    def li():
        return list(input())

    class Eratos:

        def __init__(self, num):
            assert num >= 1
            self.table_max = num
            self.table = [False if i == 0 or i == 1 else True for i in range(num + 1)]
            for i in range(2, int(math.sqrt(num)) + 1):
                if self.table[i]:
                    for j in range(i ** 2, num + 1, i):
                        self.table[j] = False
            self.prime_numbers = [2] if self.table_max >= 2 else []
            for i in range(3, self.table_max + 1, 2):
                if self.table[i]:
                    self.prime_numbers.append(i)

        def is_prime(self, num):
            """
            >>> e = Eratos(100)
            >>> [i for i in range(1, 101) if e.is_prime(i)]
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            """
            assert num >= 1
            if num > self.table_max:
                raise ValueError('Eratos.is_prime(): exceed table_max({}). got {}'.format(self.table_max, num))
            return self.table[num]

        def prime_factorize(self, num):
            """
            >>> e = Eratos(10000)
            >>> e.prime_factorize(6552)
            {2: 3, 3: 2, 7: 1, 13: 1}
            """
            assert num >= 1
            if int(math.sqrt(num)) > self.table_max:
                raise ValueError('Eratos.prime_factorize(): exceed prime table size. got {}'.format(num))
            factorized_dict = dict()
            candidate_prime_numbers = [i for i in range(2, int(math.sqrt(num)) + 1) if self.is_prime(i)]
            for p in candidate_prime_numbers:
                if num == 1:
                    break
                while num % p == 0:
                    num //= p
                    try:
                        factorized_dict[p]
                    except KeyError:
                        factorized_dict[p] = 0
                    finally:
                        factorized_dict[p] += 1
            if num != 1:
                factorized_dict[num] = 1
            return factorized_dict
    (n, m) = mi()
    eratos = Eratos(max(int(math.sqrt(m)), n))
    d = eratos.prime_factorize(m)
    FACT = [1] * (n + int(math.log2(m)) + 1)
    for i in range(2, n + int(math.log2(m)) + 1):
        FACT[i] = FACT[i - 1] * i % mod

    def comb(n, r, m):
        numerator = FACT[n]
        denominator = pow(FACT[n - r] * FACT[r], m - 2, m)
        return numerator * denominator % m
    ans = 1
    for (_, k) in list(d.items()):
        ans = ans * comb(k + n - 1, k, mod) % mod
    print(ans)


def __starting_point():
    main()


__starting_point()
