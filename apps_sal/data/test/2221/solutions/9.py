rose = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


class Solution:

    def __init__(self):
        self.wind_cost = one_cycle()
        self.wind_len = len(wind)

    def calc(self, days):
        ncycles = days // self.wind_len
        wind_x = x1 + ncycles * self.wind_cost[0]
        wind_y = y1 + ncycles * self.wind_cost[1]
        (wind_x, wind_y) = rest([wind_x, wind_y], days % self.wind_len)
        return abs(wind_x - x2) + abs(wind_y - y2)

    def __getitem__(self, days):
        return self.calc(days) <= days


def one_cycle():
    p = [0, 0]
    for w in wind:
        p[0] += rose[w][0]
        p[1] += rose[w][1]
    return p


def rest(p, k):
    for i in range(k):
        p[0] += rose[wind[i]][0]
        p[1] += rose[wind[i]][1]
    return p


def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


(x1, y1) = list(map(int, input().split()))
(x2, y2) = list(map(int, input().split()))
n = int(input())
wind = input()
k = bisect_left(Solution(), 1, 0, 100000000000000000)
if k == 100000000000000000:
    k = -1
print(k)
