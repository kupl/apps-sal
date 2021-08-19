import fractions


class Solution:

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        self.normalize(A, B)
        multiples_before_lcm = self.get_multiples_before_lcm(A, B)
        mod = 10 ** 9 + 7
        (div, rem) = (N // self.num_before_lcm, N % self.num_before_lcm)
        return (div * self.lcm + multiples_before_lcm[rem]) % mod

    def normalize(self, A, B):
        self.gcd = fractions.gcd(A, B)
        self.lcm = A * B // self.gcd
        self.normA = A // self.gcd
        self.normB = B // self.gcd
        self.num_before_lcm = self.normA + self.normB - 1

    def get_multiples_before_lcm(self, A, B):
        nextAmult = A
        nextBmult = B
        multiples = self.num_before_lcm * [None]
        multiples[0] = 0
        i = 1
        while nextAmult < self.lcm and nextBmult < self.lcm:
            if nextAmult < nextBmult:
                multiples[i] = nextAmult
                nextAmult += A
            else:
                multiples[i] = nextBmult
                nextBmult += B
            i += 1
        while nextAmult < self.lcm:
            multiples[i] = nextAmult
            nextAmult += A
            i += 1
        while nextBmult < self.lcm:
            multiples[i] = nextBmult
            nextBmult += B
            i += 1
        assert i == self.num_before_lcm
        return multiples
