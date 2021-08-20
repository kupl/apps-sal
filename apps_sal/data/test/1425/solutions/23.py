from collections import deque
n = int(input())
a = sorted(map(int, input().strip().split()))


def solve(a):
    d = deque()
    test = 0
    for i in a:
        if test:
            d.appendleft(i)
            test = 0
        else:
            d.append(i)
            test = 1
    d = list(d)
    if all((a < b + c for (a, b, c) in zip(d, d[1:] + [d[0]], [d[-1]] + d))):
        print('YES')
        print(*d)
    else:
        print('NO')


solve(a)
