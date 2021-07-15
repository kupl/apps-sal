import sys
from collections import defaultdict

#sys.stdin = open('input')


def main():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    current_sequence = defaultdict(list)
    total_subsequences = 0
    default = [0, 0]
    for elem in a:
        previous = elem / k
        if elem not in current_sequence:
            current_sequence[elem] = default.copy()
        total_subsequences += current_sequence.get(previous, default)[0]
        current_sequence[elem][0] += current_sequence.get(previous, default)[1]
        current_sequence[elem][1] += 1
    print(total_subsequences)

main()

