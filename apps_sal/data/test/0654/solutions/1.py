import sys

sys.setrecursionlimit(10 ** 9)


def fun(plus, cnt):
    if check[plus][cnt]:
        return check[plus][cnt]
    val = 0
    if plus < n and 2 * n - cnt > plus:
        val += fun(plus + 1, cnt + 1)
    if plus > 0:
        val += fun(plus - 1, cnt + 1)
    check[plus][cnt] = val
    if cnt % 2:
        check[plus][cnt] += 1
    check[plus][cnt] %= (10 ** 9 + 7)
    return check[plus][cnt]


n = int(input())
check = [[0 for _ in range(2 * n + 1)] for _ in range(2 * n + 1)]
print(fun(1, 1) % (10 ** 9 + 7))
