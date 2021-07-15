#!/usr/bin/env python3
# coding: utf-8

def debug(arg):
    if __debug__:
        pass
    else:
        import sys
        print(arg, file=sys.stderr)
        
def main():
    N, K, C = map(int, input().split())
    S = dict(enumerate(str(input()), 1))

    sr = list(k for k, v in S.items() if v == 'o')
    sl = list(reversed(sr.copy()))

    debug(sr)
    debug(sl)

    l = [sl.pop()]
    r = [sr.pop()]
    
    for x in range(1, K):
        while True:
            ll = sl.pop()
            if ll > l[x - 1] + C:
                l.append(ll)
                break
        while True:
            rr = sr.pop()
            if rr < r[x - 1] - C:
                r.append(rr)
                break

    debug(r)
    debug(l)

    # a = sorted(set(l) & set(r))

    # debug(a)
    # for aa in a:
    #     print(aa)
    
    for ll, rr in zip(l, sorted(r)):
        if ll == rr:
            print(ll)

def __starting_point():
    main()
__starting_point()
