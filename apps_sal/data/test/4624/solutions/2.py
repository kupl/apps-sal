
import math


def solve():
    n, x = list(map(int, input().split()))
    ans = 1
    n -= 2
    while n > 0:
        ans += 1
        n -= x
    print(ans)


t = 1
t = int(input())
for _ in range(0, t):
    solve()
