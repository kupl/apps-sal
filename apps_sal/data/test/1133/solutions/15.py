from collections import defaultdict
from itertools import combinations


def main():
    n = int(input())
    d = defaultdict(lambda: 0)
    for i in range(n):
        s = input()
        c1 = c2 = None
        for c in s:
            if c not in (c1, c2):
                if c1 is None:
                    c1 = c
                elif c2 is None:
                    c2 = c
                else:
                    break
        else:
            if c2 is not None:
                a = ord(c1) - 97
                b = ord(c2) - 97
                d[min(a, b), max(a, b)] += len(s)
            else:
                a = ord(c1) - 97
                for j in range(26):
                    d[min(a, j), max(a, j)] += len(s)
    result = 0
    for (a, b) in combinations(list(range(26)), 2):
        result = max(result, d[a, b])
    print(result)


try:
    while True:
        main()
except EOFError:
    pass
