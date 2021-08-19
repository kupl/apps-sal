n = int(input())
d = input()
x = list(map(int, input().split()))
inf = 10 ** 10


def solve():
    if n == 1:
        return -1
    ret = inf
    for i in range(1, n):
        if d[i - 1] == 'R' and d[i] == 'L':
            ret = min(ret, (x[i] - x[i - 1]) // 2)
    if ret == inf:
        return -1
    return ret


print(solve())
