from fractions import Fraction
from itertools import combinations
N = int(input())
YL = list(map(int, input().strip().split()))
YM = dict(enumerate(YL, start=1))


def get_b(k, x):
    y = YM[x]
    b = y - k * x
    return b


def extract(x1, x2):
    y1 = YM[x1]
    y2 = YM[x2]
    k = Fraction(y2 - y1, x2 - x1)
    b = get_b(k, x1)
    return (k, b)


def fits(k, b, x):
    return get_b(k, x) == b


def fits3(x1, x2, x):
    (k, b) = extract(x1, x2)
    return fits(k, b, x)


def getk5():
    k_count = {}
    num = min(5, N)
    for (x1, x2) in combinations(list(range(1, num + 1)), 2):
        (k, _) = extract(x1, x2)
        k_count[k] = k_count.get(k, 0) + 1
    for (k, count) in list(k_count.items()):
        if count > 2:
            return k
    return None


def main():
    if N == 3:
        print('Yes' if not fits3(1, 2, 3) else 'No')
        return
    k = getk5()
    if k is None:
        if N == 4:
            x1 = 1
            for x2 in (2, 3, 4):
                (k12, b12) = extract(x1, x2)
                (x3, x4) = [x for x in (1, 2, 3, 4) if x != x1 and x != x2]
                (k34, b34) = extract(x3, x4)
                if k12 == k34 and b12 != b34:
                    print('Yes')
                    return
            print('No')
            return
        print('No')
        return
    b_set = set()
    for x in range(1, N + 1):
        b_set.add(get_b(k, x))
    print('Yes' if len(b_set) == 2 else 'No')


main()
