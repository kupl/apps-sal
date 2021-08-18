"""E."""

import sys


def input() -> str:
    """Input."""
    return sys.stdin.readline()[:-1]


RESULT_TEXT = {
    1: 'pairwise coprime',
    2: 'setwise coprime',
    3: 'not coprime',
}

n = int(input())

a_list = list(map(int, input().split(' ')))

ans = 0

MAX = 1000000 + 1
counts = [0] * MAX
for a in a_list:
    counts[a] += 1

max_count = 0

for i in range(2, MAX):
    max_count = max(max_count, sum(counts[i::i]))

if max_count == n:
    ans = 3
elif max_count >= 2:
    ans = 2
else:
    ans = 1

print((RESULT_TEXT[ans]))
