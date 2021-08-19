from collections import defaultdict as dd
import sys
input = sys.stdin.readline
t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    st = 0
    for i in range(n):
        if l[i] > 0:
            st += l[i]
        elif st:
            mi = min(st, -l[i])
            st -= mi
    print(st)
    t -= 1
