
import math
from collections import Counter


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    counter = Counter()
    zero = 0
    for i in range(n):
        if a[i] == 0 and b[i] == 0:
            zero += 1
        elif a[i] != 0 and b[i] == 0:
            counter[0] += 1
        elif a[i] != 0 and b[i] != 0:
            g = math.gcd(a[i], b[i])
            x, y = a[i] // g, b[i] // g,
            mask = (x * y) > 0
            counter[(mask, abs(x), abs(y))] += 1

    ret = 0
    for k, v in list(counter.items()):
        ret = max(ret, v)
    print(ret + zero)


def __starting_point():
    main()


__starting_point()
