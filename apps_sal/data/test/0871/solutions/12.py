def to_minutes(h, m):
    return h * 60 + m


def to_retard(m):
    return divmod(m, 60)


(n, s) = [int(i) for i in input().split(' ')]
takeoffs = []
for i in range(n):
    takeoff_time = to_minutes(*[int(i) for i in input().split(' ')])
    takeoffs.append(takeoff_time)


def solve():
    if takeoffs[0] > s:
        return 0
    for i in range(n - 1):
        if takeoffs[i + 1] - takeoffs[i] - 1 >= 2 * s + 1:
            return takeoffs[i] + s + 1
    return takeoffs[-1] + s + 1


print(*to_retard(solve()))
