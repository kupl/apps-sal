class Cumsum2d(object):

    def __init__(self, a):
        self.a = a
        self.h = len(a)
        self.w = len(a[0])
        self._cumsum = [[0 for _ in range(self.w + 1)] for _ in range(self.h + 1)]
        self._preprocess()

    def _preprocess(self):
        for i in range(1, self.h + 1):
            for j in range(1, self.w + 1):
                self._cumsum[i][j] = self.a[i - 1][j - 1] + self._cumsum[i][j - 1] + self._cumsum[i - 1][j] - self._cumsum[i - 1][j - 1]

    def query(self, h1, h2, w1, w2):
        return self._cumsum[h2][w2] - self._cumsum[h1][w2] - self._cumsum[h2][w1] + self._cumsum[h1][w1]


def __starting_point():
    (N, M, Q) = [int(x) for x in input().split(' ')]
    count = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for _ in range(M):
        (l, r) = [int(x) for x in input().split(' ')]
        count[l][r] += 1
    cumsum = Cumsum2d(count)
    for _ in range(Q):
        (p, q) = [int(x) for x in input().split(' ')]
        print(cumsum.query(p, q + 1, p, q + 1))


__starting_point()
