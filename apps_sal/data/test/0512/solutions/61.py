# Reference: https://atcoder.jp/contests/arc104/submissions/17167838
import sys
from functools import lru_cache

sys.setrecursionlimit(100000)


@lru_cache(None)
def dfs(f):
    if f == 2 * n + 1:
        return True
    
    max_up = (2 * n - f + 1) // 2
    for up in range(1, max_up + 1):
        for i in range(f, f + up):
            if floors[i] < 0:
                # Fail by off at bottom half of segment
                break
            if floors[i + up] > 0:
                # Fail by on at top half of segment
                break
            if floors[i] != 0 and floors[i + up] != 0 and floors[i] != -1 * floors[i + up]:
                # In segment not matched on and off
                break
        else:
            # Check uppper segment with just passed this segment f with up.
            # Every person in this segment off after up amount.
            if dfs(f + 2 * up):
                return True
            else:
                # Fail to satisfy in any upper segments, then continue to next possible up at f.
                pass
    return False


n = int(input())
floors = [0] * (2 * n + 1)

for i in range(1, n + 1):
    a, b = map(int, input().split())
    if a != -1:
        if floors[a] != 0:
            print('No')
            return
        floors[a] = i
    if b != -1:
        if floors[b] != 0:
            print('No')
            return
        floors[b] = -i

print('Yes' if dfs(1) else 'No')
