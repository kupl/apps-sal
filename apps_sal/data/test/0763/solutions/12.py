import math
import sys
import itertools


def mp():
    return list(map(int, input().split()))


def main():
    n = int(input())
    a = mp()
    ans = int(1000000000.0)
    for i in range(n):
        res = 0
        for j in range(n):
            res += a[j] * (2 * i + 2 * abs(i - j) + 2 * j)
        ans = min(ans, res)
    print(ans)


deb = 0
if deb:
    file = open('input.txt', 'r')
    input = file.readline
else:
    input = sys.stdin.readline
main()
