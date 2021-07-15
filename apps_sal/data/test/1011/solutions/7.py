from itertools import chain
from bisect import bisect_left as bisect


def main():
    n = int(input().strip())
    aa = list(map(int, input().strip().split()))
    aa.sort()
    m = int(input().strip())
    bb = list(map(int, input().strip().split()))
    bb.sort()
    res = []
    dd = set(chain(aa, bb))
    for d in chain(aa, bb):
        dd.add(d + 1)
    la = len(aa) * 3
    lb = len(bb) * 3
    for d in dd:
        a = la - bisect(aa, d)
        b = lb - bisect(bb, d)
        res.append((a - b, a))
    b, a = max(res)
    print('{:n}:{:n}'.format(a, a - b))


main()
