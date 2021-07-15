from collections import defaultdict
from itertools import groupby


def reverse_enumerate(seq):
    n = len(seq)
    for i in range(n):
        yield n - 1 - i, seq[n - 1 - i]


class Symbol(object):
    def __init__(self, symbol, iter=None):
        self.symbol = symbol
        self.size = sum(1 for _ in iter) if iter else 0

    def __hash__(self):
        return hash(self.symbol)


def solve(inp):
    symbols = [Symbol(s, i) for s, i in groupby(inp)]
    longest_end_a = defaultdict(int)
    longest_start_a = defaultdict(int)
    longest_end_b = defaultdict(int)
    n = len(symbols)
    if n == 1:
        return len(inp)
    for idx, symbol in reverse_enumerate(symbols):
        if symbol.symbol == "a":
            longest_end_a[idx] = longest_end_a[idx + 1] + symbol.size
            longest_end_b[idx] = longest_end_b[idx + 1]
        else:
            longest_end_a[idx] = longest_end_a[idx + 1]
            longest_end_b[idx] = longest_end_b[idx + 1] + symbol.size
    for idx, symbol in enumerate(symbols):
        if symbol.symbol == "a":
            longest_start_a[idx] = longest_start_a[idx - 1] + symbol.size
        else:
            longest_start_a[idx] = longest_start_a[idx - 1]
    return max(
        longest_start_a[idx] + (longest_end_b[idx] - longest_end_b[second_idx]) + longest_end_a[second_idx]
        for idx in range(n)
        for second_idx in range(idx + 1, n + 1)
    )


def __starting_point():
    print(solve(input()))
__starting_point()
