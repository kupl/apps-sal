import math
import collections
import sys
input = sys.stdin.readline


def solve():
    (n, m) = map(int, input().split())
    if n % m:
        print('NO')
    else:
        print('YES')


for _ in range(int(input())):
    solve()
