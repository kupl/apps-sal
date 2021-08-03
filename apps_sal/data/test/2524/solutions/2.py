import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    for i in range(60):
        cnt_one = 0
        for a in A:
            if (a >> i) & 1:
                cnt_one += 1
        res += (n - cnt_one) * cnt_one * pow(2, i)
        res %= mod
    print(res)


def __starting_point():
    resolve()


__starting_point()
