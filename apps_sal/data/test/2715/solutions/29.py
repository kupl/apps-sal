import sys
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def in_n():
    return int(readline())


def in_nn():
    return list(map(int, readline().split()))


def in_s():
    return readline().rstrip().decode('utf-8')


def in_nl():
    return list(map(int, readline().split()))


def in_nl2(H):
    return [in_nl() for _ in range(H)]


def in_map():
    return [s == ord('.') for s in readline() if s != ord('\n')]


def in_map2(H):
    return [in_map() for _ in range(H)]


def in_all():
    return list(map(int, read().split()))


def main():
    K = in_n()
    N = 50
    (q, r) = divmod(K, N)
    ans = np.full(N, N + q)
    cnt = N - r
    ans[:cnt] -= N - (cnt - 1)
    ans[cnt:] += cnt
    print(N)
    print(' '.join(map(str, ans)))


def __starting_point():
    main()


__starting_point()
