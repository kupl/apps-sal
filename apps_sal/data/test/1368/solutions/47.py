class cmbs(object):

    def __init__(self, mod=9007199254740997):
        self.mod = mod
        self.g1 = [1, 1]
        self.g2 = [1, 1]
        inverse = [0, 1]
        for i in range(2, 10 ** 2 + 1):
            self.g1.append(self.g1[-1] * i % mod)
            inverse.append(-inverse[mod % i] * (mod // i) % mod)
            self.g2.append(self.g2[-1] * inverse[-1] % mod)

    def cmb(self, n, r):
        if n > 10 ** 6:
            return self.cmbl(n, r)
        return self.cmbr(n, r)

    def cmbr(self, n, r):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return self.g1[n] * self.g2[r] * self.g2[n - r] % self.mod


def main():
    (N, A, B) = list(map(int, input().split()))
    v = list(map(int, input().split()))
    v.sort(reverse=True)
    m = sum(v[:A]) / A
    print(m)
    if v.count(v[A - 1]) == N:
        c = cmbs()
        a = 0
        for i in range(A, B + 1):
            a += c.cmb(N, i)
        print(a)
    elif v[0] == v[A - 1]:
        c = cmbs()
        a = 0
        for i in range(A, min(v.count(v[A - 1]), B) + 1):
            a += c.cmb(v.count(v[A - 1]), i)
        print(a)
    elif v.count(v[A - 1]) == 1:
        print(1)
    else:
        c = cmbs()
        r = A - v.index(v[A - 1])
        print(c.cmb(v.count(v[A - 1]), r))


main()
