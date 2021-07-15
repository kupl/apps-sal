import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from itertools import product
def main():
    h, w, k = list(map(int, input().split()))
    gg = []
    for _ in range(h):
        row = [1 if c == '#' else 0 for c in list(input())]
        gg.extend(row)
    row_pro = tuple(product((0, 1), repeat=h))
    col_pro = tuple(product((0, 1), repeat=w))
    rows = []
    for re in row_pro:
        rows.append([i for i, b in enumerate(re) if b])
    cols = []
    for ce in col_pro:
        cols.append([i for i, b in enumerate(ce) if b])
    pat = tuple(product(rows, cols))
    r = 0
    for pate in pat:
        t0 = 0
        for p0 in pate[0]:
            for p1 in pate[1]:
                t0 += gg[p0*w + p1]
        if t0 == k:
            r += 1
    print(r)

def __starting_point():
    main()

__starting_point()
