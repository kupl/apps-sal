from itertools import product, accumulate, combinations, product
import sys
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = 1 << 50
EPS = 1e-08
mod = 10 ** 9 + 7


def run():
    N = int(input())
    nines = [9 ** i for i in range(1, 10) if 9 ** i <= N]
    sixes = [6 ** i for i in range(1, 10) if 6 ** i <= N][::-1]
    L = len(nines)
    min_ans = INF
    for K in product(list(range(9)), repeat=L):
        ans = 0
        s = 0
        for (k, x) in zip(K, nines):
            if k:
                ans += k
                s += x * k
        if s > N:
            continue
        resid = N - s
        for six in sixes:
            tmp = resid // six
            if tmp:
                ans += tmp
                resid -= six * tmp
        ans += resid
        min_ans = min(min_ans, ans)
    print(min_ans)


def __starting_point():
    run()


__starting_point()
