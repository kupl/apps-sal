from collections import Counter


def increment_counter(counter, key):
    counter[key] += 1


def decrement_counter(counter, key):
    if key in counter:
        counter[key] -= 1
        if counter[key] == 0:
            del counter[key]


def naive_solution(s: str) -> int:

    total = Counter(s)
    count = 0

    p = Counter()
    for char in s:
        p[char] += 1

        q = total - p

        if len(p) == len(q):
            count += 1

    return count


def optimized(s: str) -> int:
    prefix = Counter()
    suffix = Counter(s)
    count = 0
    for char in s:
        increment_counter(prefix, char)
        decrement_counter(suffix, char)

        if len(prefix) == len(suffix):
            count += 1

    return count


class Solution:
    def numSplits(self, s: str) -> int:
        return optimized(s)
