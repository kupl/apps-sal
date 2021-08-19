from collections import deque


def solve(a):
    ans = deque()
    for (i, aa) in enumerate(a):
        if i % 2 == 0:
            ans.append(str(aa))
        else:
            ans.appendleft(str(aa))
    if len(a) % 2 == 1:
        ans.reverse()
    return list(ans)


def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))
    print(' '.join(solve(a)))


__starting_point()
