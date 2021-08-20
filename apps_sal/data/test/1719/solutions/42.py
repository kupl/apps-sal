from collections import defaultdict
from functools import reduce


def main():
    m = 10 ** 9 + 7
    n = int(input())
    current = defaultdict(int)
    current['TTT'] = 1
    for i in range(n):
        wip = defaultdict(int)
        for c in 'AGCT':
            for (k, v) in current.items():
                if k + c in ['ATGC', 'AGTC', 'AGGC']:
                    continue
                z = k[1:] + c
                if z in ['AGC', 'ACG', 'GAC']:
                    continue
                wip[z] = (wip[z] + v) % m
        current = wip
    print(reduce(lambda acc, x: (acc + x) % m, wip.values()))


main()
