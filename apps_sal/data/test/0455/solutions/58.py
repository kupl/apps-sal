import sys
import math
import collections
import heapq
import itertools


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0:
        a, b = b, a % b
    return b


def solve():
    file = sys.stdin.readline  # single: int(file()), line: map(int, file().split())
    N = int(file())
    point = [[int(i) for i in file().split()] for j in range(N)]
    length = (point[0][0] + point[0][1]) % 2
    for i in range(1, N):
        if sum(point[i]) % 2 != length:
            print(-1)
            break
    else:
        d = [pow(2, i) for i in range(31)]
        direction = {("0", "0"): "L", ("1", "1"): "R", ("0", "1"): "D", ("1", "0"): "U"}
        ans = ""
        add = (0 if length == 1 else 1)
        if add == 1:
            d.append(1)
        for i in range(N):
            U, V = point[i][0] + point[i][1] + add, point[i][0] - point[i][1] + add
            ubit = format((U + pow(2, 31) - 1) // 2, "b").zfill(31)
            vbit = format((V + pow(2, 31) - 1) // 2, "b").zfill(31)
            arm = ""
            for j in reversed(range(31)):
                arm += direction[(ubit[j], vbit[j])]
            if add == 1:
                arm += "L"
            ans += arm + "\n"
        print(len(d))
        print(" ".join(map(str, d)))
        print(ans)

    INF = 10 ** 25
    mod = 7 + 10 ** 9
    return 0


def __starting_point():
    solve()


__starting_point()
