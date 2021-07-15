import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, A, B = mapint()
from collections import deque
if A+B-1>N or N>A*B:
    print(-1)
else:
    blocks = []
    blocks.append(' '.join(map(str, range(B, 0, -1))))
    now = B+1
    rest = N-A+2

    while now:
        if now==rest:
            break
        if now+B>rest:
            blocks.append(' '.join(map(str, range(rest, now-1, -1))))
            rest += 1
            break
        blocks.append(' '.join(map(str, range(now+B-1, now-1, -1))))
        now = now+B
        rest += 1
    blocks.append(' '.join(map(str, range(rest, N+1))))
    print(' '.join(blocks))
