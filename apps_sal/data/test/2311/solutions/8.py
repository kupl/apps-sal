import bisect
import sys
from collections import Counter
sys.setrecursionlimit(100000)
input = sys.stdin.readline
INF = 2 ** 62 - 1


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()
        error_print(e - s, 'sec')
        return ret
    return wrap


def divisor(n):
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield (n // i)


@mt
def slv(N, M, K, A, B):
    ans = 0
    ca = [0]
    for v in A:
        if v == 1:
            ca[-1] += 1
        else:
            ca.append(0)
    cb = [0]
    for v in B:
        if v == 1:
            cb[-1] += 1
        else:
            cb.append(0)
    ca = Counter(ca)
    cb = Counter(cb)
    ans += 0
    for d in divisor(K):
        e = K // d
        for (i, x) in ca.items():
            for (j, y) in cb.items():
                if i < d or j < e:
                    continue
                ans += (i - d + 1) * (j - e + 1) * x * y
    return ans


def main():
    (N, M, K) = read_int_n()
    A = read_int_n()
    B = read_int_n()
    print(slv(N, M, K, A, B))


def __starting_point():
    main()


__starting_point()
