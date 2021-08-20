def binary_search_first_true(predicate, from_inclusive, to_inclusive):
    lo = from_inclusive - 1
    hi = to_inclusive + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if not predicate(mid):
            lo = mid
        else:
            hi = mid
    return hi


def tri(n):
    return n * (n + 1) // 2


def f(n, m, t):
    return n - tri(t - m - 1) - t


def solve(n, m):
    if m >= n:
        return n
    ans = binary_search_first_true(lambda x: f(n, m, x) <= 0, m + 1, n)
    return ans


def main(sc):
    (n, m) = sc.next_ints(2)
    ans = solve(n, m)
    print(ans)


class Scanner:

    def __init__(self):
        self.idx = 0
        self.tokens = []

    def __next__(self):
        while self.idx == len(self.tokens) or not len(self.tokens[self.idx]):
            if self.idx == len(self.tokens):
                self.idx = 0
                self.tokens = input().split()
            else:
                self.idx += 1
        self.idx += 1
        return self.tokens[self.idx - 1]

    def next_string(self):
        return next(self)

    def next_strings(self, n):
        return [self.next_string() for i in range(0, n)]

    def next_int(self):
        return int(next(self))

    def next_ints(self, n):
        return [self.next_int() for i in range(0, n)]


scanner = Scanner()
main(scanner)
