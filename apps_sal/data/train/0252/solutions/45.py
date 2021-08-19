def redundant(a, b):
    ((al, ar), (bl, br)) = (a, b)
    return al <= bl <= br <= ar or bl <= al <= ar <= br


def union(a, b):
    ((al, ar), (bl, br)) = (a, b)
    return (min(al, bl), max(ar, br))


def remove_overlap(ranges):
    ans = []
    for rng in ranges:
        ans.append(rng)
        while len(ans) >= 2 and redundant(ans[-2], ans[-1]):
            b = ans.pop()
            a = ans.pop()
            ans.append(union(a, b))
    return ans


def union_covers(a, b, c):
    ((al, ar), (bl, br), (cl, cr)) = (a, b, c)
    return al <= cl <= ar <= cr and al <= bl <= br <= cr


def min_taps(n, radii):
    assert n >= 1
    assert len(radii) == n + 1
    ranges = []
    for (center, radius) in enumerate(radii):
        if radius > 0:
            left_end = max(0, center - radius)
            right_end = min(n, center + radius)
            ranges.append((left_end, right_end))
    ranges = remove_overlap(ranges)
    final_ranges = []
    for rng in ranges:
        if len(final_ranges) >= 2 and union_covers(final_ranges[-2], final_ranges[-1], rng):
            final_ranges.pop()
        final_ranges.append(rng)
    if final_ranges and final_ranges[0][0] == 0 and (final_ranges[-1][-1] == n) and all((final_ranges[i][1] >= final_ranges[i + 1][0] for i in range(len(final_ranges) - 1))):
        return len(final_ranges)
    else:
        return -1


class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        return min_taps(n, ranges)
