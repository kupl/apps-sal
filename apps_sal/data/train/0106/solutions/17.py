import math


def is_intersect(l1, r1, l2, r2):
    return (l1 < l2 and r1 >= l2) or (l1 >= l2 and l1 <= r2)


def get_groups(ranges):
    ranges.sort(key=lambda x: x[1])
    ranges.sort(key=lambda x: x[0])
    ranges[0][3] = 1
    group1 = ranges[0][:2]
    group2 = None
    for i, rng in enumerate(ranges[1:]):
        l, r = rng[:2]
        if is_intersect(l, r, *group1) and ((group2 is None) or not is_intersect(l, r, group2)):
            rng[3] = 1
            group1[0] = min(group1[0], l)
            group1[1] = max(group1[1], r)
        elif not is_intersect(l, r, *group1):
            if group2 is None:
                group2 = [l, r]
            else:
                group2[0] = min(group2[0], l)
                group2[1] = max(group2[1], r)
            rng[3] = 2
        else:
            return -1
    if group2 is None:
        return -1
    ranges.sort(key=lambda x: x[2])
    return ' '.join(list(map(str, (rng[3] for rng in ranges))))


def __starting_point():
    n = int(input())
    for i in range(n):
        k = int(input())
        arr = [None] * k
        for j in range(k):
            arr[j] = list(map(int, input().split())) + [j, -1]
        print(get_groups(arr))


__starting_point()
