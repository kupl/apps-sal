import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

INF = -(2 ** 31)

N, C = [int(_) for _ in input().split()]
X = [[int(x) for x in input().split()] for _ in range(N)]


def spam():
    L = [0] * N
    pre = 0
    pre_max = -(2 ** 31)
    for i in range(N):
        x, v = X[-i - 1]
        L[i] = max(pre_max, pre + v - (C - x))
        pre += v
        pre_max = L[i]

    ans = max(pre_max, 0)
    pre = 0
    for i in range(N):
        x, v = X[i]
        tmp = pre + v - x

        if i < N - 1:
            tmp2 = max(L[N - i - 2] - x, 0)
        else:
            tmp2 = 0
        ans = max(ans, tmp + tmp2)
        pre += v
    return ans


def main():
    nonlocal X
    ans = spam()
    X = X[::-1]
    for i in range(N):
        X[i][0] = C - X[i][0]
    ans = max(ans, spam())
    print(ans)


main()

