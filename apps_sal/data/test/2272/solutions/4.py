def get_operations():
    n = int(input())
    return [tuple((int(k) for k in input().split())) for _ in range(n)]


def can_move(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return x2 < x1 and x1 < y2 or (x2 < y1 and y1 < y2)


def can_reach(intervals, x, y, mask=[]):
    if not mask:
        mask = [False] * len(intervals)
    if x == y:
        return True
    mask[x] = True
    xs = [k for k in range(len(intervals)) if not mask[k] and can_move(intervals[x], intervals[k])]
    return any((can_reach(intervals, k, y, mask) for k in xs))


def solve(operations):
    intervals = []
    results = []
    for op in operations:
        (t, x, y) = op
        if t == 1:
            intervals.append(tuple([x, y]))
        else:
            results.append(can_reach(intervals, x - 1, y - 1))
    return results


def __starting_point():
    operations = get_operations()
    results = solve(operations)
    for res in results:
        print('YES' if res else 'NO')


__starting_point()
