import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = list(map(int, input().split()))
    s = input()

    cnt = 0
    score = 0
    for i in range(1, n):
        if s[i - 1] != s[i]:
            cnt += 1
        else:
            score += 1

    res = min(n - 1, score + min(k, cnt) * 2)
    print(res)


def __starting_point():
    resolve()

__starting_point()
