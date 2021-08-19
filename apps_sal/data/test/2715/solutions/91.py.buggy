import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k = int(input())
    S = list(range(50))
    k, r = divmod(k, 50)
    for i in range(50):
        S[i] += k

    target = 0
    while r:
        for i in range(50):
            if i == target:
                S[i] += 50
            else:
                S[i] -= 1
        target = (target + 1) % 50
        r -= 1
    print((50))
    print((*S))


def __starting_point():
    resolve()


__starting_point()
