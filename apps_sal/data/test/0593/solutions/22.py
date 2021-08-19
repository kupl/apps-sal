import sys
sys.setrecursionlimit(1000000)


def solve():
    (n, m) = rv()
    citieswon = [0] * n
    for city in range(m):
        (a,) = rl(1)
        index = 0
        for i in range(n):
            if a[i] > a[index]:
                index = i
        citieswon[index] += 1
    cityindex = 0
    for i in range(n):
        if citieswon[i] > citieswon[cityindex]:
            cityindex = i
    print(cityindex + 1)


def rv():
    return list(map(int, input().split()))


def rl(n):
    return [list(map(int, input().split())) for _ in range(n)]


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
solve()
