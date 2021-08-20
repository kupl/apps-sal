class Solution:

    def check_prime(self, N):
        m = int(math.sqrt(N))
        for i in range(2, m + 1):
            if N % i == 0:
                return 0
        return 1

    def reverse_string(self, s):
        n = len(s)
        t = [s[n - i] for i in range(1, n + 1)]
        t = ''.join(t)
        return t

    def rev(self, l, parity):
        l = [str(s) for s in l]
        if parity == 0:
            l = [s + self.reverse_string(s) for s in l]
        if parity == 1:
            l = [s[:-1] + s[-1] + self.reverse_string(s[:-1]) for s in l]
        return l

    def gen_palin(self, k):
        m = k // 2
        parity = k % 2
        if k % 2 == 0:
            l = list(range(10 ** (m - 1), 10 ** m))
        if k % 2 == 1:
            l = list(range(10 ** m, 10 ** (m + 1)))
        l = self.rev(l, parity)
        l = [int(x) for x in l]
        l.sort()
        return l

    def primePalindrome(self, N):
        if N == 1:
            return 2
        s = str(N)
        k = len(s)
        current = k
        x = 1
        while x:
            l = self.gen_palin(k)
            for a in l:
                if a >= N:
                    if self.check_prime(a):
                        return a
            k += 1
