import sys
import socket

hostnames = ['N551J', 'F551C', 'X553M']
input_file = 'e1.in'
if socket.gethostname() in hostnames:
    sys.stdin = open(input_file)


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()

inf = 10 ** 9
inf = 10 ** 3

def solve():
    n = read_int()
    a = read_int_list()
    b = [(a[i], i) for i in range(n)]
    b.sort()
    best = [[-inf] * (n + 1) for i in range(n + 1)]
    best[0][0] = 0
    for s in range(1, n + 1):
        for x in range(s + 1):
            y = s - x
            ai, i = b[-s]
            if x > 0:
                c = best[x - 1][y] + (n - x) * ai - i * ai
                if c > best[x][y]:
                    best[x][y] = c
            if y > 0:
                c = best[x][y - 1] - (y - 1) * ai + i * ai
                if c > best[x][y]:
                    best[x][y] = c

    # for i in range(n + 1):
    #     for j in range(n + 1):
    #         print(best[i][j], end='\t')
    #     print()

    res = - inf
    for x in range(n):
        y = n - x
        if res < best[x][y]:
            res = best[x][y]
    return res


def main():
    res = solve()
    print(res)


def __starting_point():
    main()

__starting_point()
