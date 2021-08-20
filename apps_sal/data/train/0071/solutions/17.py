from math import ceil
from collections import deque
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    s = 0
    for i in range(n):
        if a[i] < s:
            ans += s - a[i]
            s = 0
        else:
            s -= a[i]
    print(ans)
