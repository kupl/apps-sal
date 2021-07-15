import sys
from collections import defaultdict


def get_lines():
    return [line for line in sys.stdin]


def get_sum_counts(K):
    cnts = defaultdict(int)
    for i in range(K + 1):
        for j in range(K + 1):
            cnts[i + j] += 1
    return cnts


def main(lines):
    '''
    S - Z = X + Y
    '''
    K, S = list(map(int, lines[0].split()))
    count = 0
    sum_counts = get_sum_counts(K)
    for z in range(min(K, S) + 1):
        target = S - z
        count += sum_counts[target]
    return count


def __starting_point():
    lines = get_lines()
    res = main(lines)
    print(f'{res}')

__starting_point()
