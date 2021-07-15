from collections import deque
from sys import stdin
lines = deque(line.strip() for line in stdin.readlines())

def nextline():
    return lines.popleft()

def types(cast, sep=None):
    return tuple(cast(x) for x in strs(sep=sep))

def ints(sep=None):
    return types(int, sep=sep)

def strs(sep=None):
    return tuple(nextline()) if sep == '' else tuple(nextline().split(sep=sep))

def main():
    # lines will now contain all of the input's lines in a list
    T = int(nextline())
    for testCase in range(1, T + 1):
        n, m, k = ints()
        min_k = max(n, m)
        if min_k > k:
            print(-1)
            continue
        if (n - m) % 2 == 0:
            if k % 2 == n % 2:
                print(k)
                continue
            print(k - 2)
            continue
        print(k - 1)

def __starting_point():
    main()

__starting_point()
