import sys


def __starting_point():
    (n, t, c) = list(map(int, sys.stdin.readline().split()))
    prisoners = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    risk = 0
    for i in range(c):
        if t < prisoners[i]:
            risk += 1
    if not risk:
        cnt += 1
    for i in range(c, n):
        if t < prisoners[i]:
            risk += 1
        if t < prisoners[i - c]:
            risk -= 1
        if not risk:
            cnt += 1
    print(cnt)


__starting_point()
