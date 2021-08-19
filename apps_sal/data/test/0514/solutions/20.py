from math import ceil
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def solve():
    (n, d) = list(map(int, input().split()))
    ans = False
    if d <= n:
        ans = True
    for i in range(-20, 21):
        x = (n - 1) // 2 + i
        if x > 0:
            if x + ceil(d / (x + 1)) <= n:
                ans = True
    if ans:
        print('YES')
    else:
        print('NO')


t = int(input())
for i in range(t):
    solve()
