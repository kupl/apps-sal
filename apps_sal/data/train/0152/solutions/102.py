def can_distribute(baskets, ball_count, min_dist):
    last = []
    for basket in baskets:
        if not last or last[-1] + min_dist <= basket:
            last.append(basket)
            if len(last) == ball_count:
                return True
    return False


def first(a, b, p):
    if a >= b:
        return a
    elif p(a):
        return a
    elif not p(b - 1):
        return b
    else:
        m = (a + b) // 2
        if p(m - 1):
            return first(a, m, p)
        elif not p(m):
            return first(m, b, p)
        else:
            return m


def last(a, b, p):
    return first(a, b, lambda x: not p(x)) - 1


def max_dist(baskets, ball_count):
    baskets = sorted(baskets)
    theoretical_max_dist = (baskets[-1] - baskets[0]) // (ball_count - 1)
    return last(1, theoretical_max_dist + 1, lambda dist: can_distribute(baskets, ball_count, dist))


class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        return max_dist(position, m)
