import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = input().strip("\n")
    ans = deque()
    current = N
    while current > 0:
        for i in reversed(range(1, M+1)):
            if current - i >= 0 and S[current - i] == "0":
                ans.appendleft(i)
                current -= i
                break
        else: break
    if current > 0: print(-1)
    else: print(*ans, sep=" ")


    return 0

def __starting_point():
    solve()
__starting_point()
