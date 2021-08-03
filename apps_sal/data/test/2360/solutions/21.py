from collections import deque


def solve(ar):
    res = []
    time = 0
    for l, r in ar:
        if r >= time:
            if time == 0:
                time = l + 1
                res.append(l)
            else:
                if l >= time:
                    time = l
                res.append(time)
                time += 1
        else:
            res.append(0)
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(deque(int(x) for x in input().split()))
    print(*solve(a))
