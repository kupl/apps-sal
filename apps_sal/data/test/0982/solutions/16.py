from collections import defaultdict as dd
import sys
input = sys.stdin.readline
t = int(input())
while t:
    (n, m) = map(int, input().split())
    if (m + 1) / 2 <= n:
        print('YES')
    else:
        print('NO')
    t -= 1
