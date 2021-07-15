__author__ = 'Andrey'


def solve(n):
    nonlocal min_1
    nonlocal min_2
    nonlocal min_3
    nonlocal max_1
    nonlocal max_2
    nonlocal max_3
    c_1, c_2, c_3 = 0, 0, 0
    c_2 += min_2
    c_3 += min_3
    n -= min_2 + min_3
    firsts = min(n, max_1)
    c_1 += firsts
    n -= firsts
    if n == 0:
        return c_1, c_2, c_3
    else:
        seconds = min(max_2 - min_2, n)
        n -= seconds
        c_2 += seconds
        if n == 0:
            return c_1, c_2, c_3
        else:
            thirds = min(max_3 - min_3, n)
            n -= thirds
            c_3 += thirds
            if n == 0:
                return c_1, c_2, c_3



n = int(input())
min_1, max_1 = map(int, input().split())
min_2, max_2 = map(int, input().split())
min_3, max_3 = map(int, input().split())
print(*solve(n))
