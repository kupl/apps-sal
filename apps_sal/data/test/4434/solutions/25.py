from collections import defaultdict as dd
import sys
input = sys.stdin.readline
t = int(input())
while t:
    n = int(input())
    a = 8
    res = 0
    for i in range(1, n // 2 + 1):
        res += a * i * i
    print(res)
    t -= 1
