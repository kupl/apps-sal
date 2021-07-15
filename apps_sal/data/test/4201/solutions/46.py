import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from itertools import product
def main():
    h, w, k = map(int, input().split())
    gg = []
    for _ in range(h):
        row = [1 if c == '#' else 0 for c in list(input())]
        gg.extend(row)
    row_pro = tuple(product((0, 1), repeat=h))
    col_pro = tuple(product((0, 1), repeat=w))
    pat = tuple(product(row_pro, col_pro))
    r = 0
    for pate in pat:
        t0 = 0
        for i0, p0 in enumerate(pate[0]):
            for i1, p1 in enumerate(pate[1]):
                if p0 and p1:
                    t0 += gg[i0*w + i1]
        if t0 == k:
            r += 1
    print(r)

def __starting_point():
    main()
__starting_point()
