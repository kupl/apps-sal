import copy


def main():
    N = int(input())
    if N == 3:
        return 61
    mod = 10 ** 9 + 7
    d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    AGC = [[[1] * 4 for _ in range(4)] for _ in range(4)]
    AGC[d['A']][d['G']][d['C']] = 0
    AGC[d['A']][d['C']][d['G']] = 0
    AGC[d['G']][d['A']][d['C']] = 0
    NAGC = [[[1] * 4 for _ in range(4)] for _ in range(4)]
    for i in range(3, N):
        for i1 in range(4):
            for i2 in range(4):
                for i3 in range(4):
                    t = 0
                    if (i2 == d['G'] or i1 == d['G']) and i3 == d['C']:
                        for i4 in range(1, 4):
                            t += AGC[i4][i1][i2]
                    else:
                        for i4 in range(4):
                            t += AGC[i4][i1][i2]
                    if i1 == d['A'] and i2 == d['G'] and (i3 == d['C']):
                        t = 0
                    if i1 == d['A'] and i2 == d['C'] and (i3 == d['G']):
                        t = 0
                    if i1 == d['G'] and i2 == d['A'] and (i3 == d['C']):
                        t = 0
                    t %= mod
                    NAGC[i1][i2][i3] = t
        AGC = copy.deepcopy(NAGC)
    return sum((sum((sum(j) for j in i)) for i in AGC)) % mod


print(main())
