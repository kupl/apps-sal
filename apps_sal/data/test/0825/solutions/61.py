from collections import defaultdict
from math import sqrt


def main():
    n = int(input())
    wi = 2
    cnt = 0
    d = defaultdict(lambda: 0)
    fi = int(sqrt(1e12) + 1)
    for i in range(2, fi):
        while n % i == 0:
            d[i] += 1
            n //= i
    if n != 1:
        d[n] = 1

    for val in d.values():
        x = val
        wi = 1
        while(x >= wi):
            x -= wi
            wi += 1
            cnt += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
