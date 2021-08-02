import math
import sys
input = sys.stdin.readline
pc = True
n = int(input())
a = list(map(int, input().split()))
g = math.gcd(a[0], a[1])
for i in range(2, n):
    g = math.gcd(g, a[i])
M = max(a)


class Sieve_of_Eratosthenes:
    def __init__(self, N):
        self.sieve = [-1] * (N + 1)

        for i in range(2, N + 1):
            if self.sieve[i] == -1:
                for j in range(1, 1 + N // i):
                    self.sieve[i * j] = i

    def isprime(self, num):
        if num <= 1:
            return False
        else:
            return self.sieve[num] == num

    def factorization(self, num):
        ret = set([])
        while num != 1:
            div = self.sieve[num]
            ret.add(div)
            num //= div
        return ret


sofe = Sieve_of_Eratosthenes(M)

judge = set([])

for i in a:
    if not pc:
        break
    asf = sofe.factorization(i)

    if judge & asf != set():
        pc = False
    judge |= asf
if pc:
    print("pairwise coprime")
elif g == 1:
    print("setwise coprime")
else:
    print("not coprime")
