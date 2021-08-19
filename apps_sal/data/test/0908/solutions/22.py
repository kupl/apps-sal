LO_C = 0
LO_S = 1
HI_C = 2
HI_S = 3


def main():
    n = int(input())
    costs = list([int(x) for x in input().split()])
    memo = list()
    for i in range(n):
        s = input().strip()
        r = s[::-1]
        if s <= r:
            (lo, lo_c, hi, hi_c) = (s, 0, r, costs[i])
        else:
            (lo, lo_c, hi, hi_c) = (r, costs[i], s, 0)
        if not memo:
            memo.append((lo_c, lo, hi_c, hi))
        else:
            if hi >= memo[-1][LO_S]:
                nxt_hi = hi
                if hi < memo[-1][HI_S] or memo[-1][LO_C] <= memo[-1][HI_C]:
                    nxt_hi_c = hi_c + memo[-1][LO_C]
                else:
                    nxt_hi_c = hi_c + memo[-1][HI_C]
            else:
                return -1
            if lo >= memo[-1][LO_S]:
                nxt_lo = lo
                if lo < memo[-1][HI_S] or memo[-1][LO_C] <= memo[-1][HI_C]:
                    nxt_lo_c = lo_c + memo[-1][LO_C]
                else:
                    nxt_lo_c = lo_c + memo[-1][HI_C]
            else:
                nxt_lo = nxt_hi
                nxt_lo_c = nxt_hi_c
            memo.append((nxt_lo_c, nxt_lo, nxt_hi_c, nxt_hi))
    return min(memo[-1][LO_C], memo[-1][HI_C])


def __starting_point():
    print(main())


__starting_point()
