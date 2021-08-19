import sys
import threading
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
threading.stack_size(16 * 2048 * 2048)
n = int(input())
a = [int(i) for i in input().split() if i != '\n']
a.insert(0, 0)
a.append(0)


def solve(l, r):
    if l > r:
        return 0
    outside = max(a[l - 1], a[r + 1])
    mina = min(a[l:r + 1])
    min_index = a.index(mina, l, r + 1)
    return min(r - l + 1, solve(l, min_index - 1) + solve(min_index + 1, r) + mina - outside)


ans = solve(1, n)
sys.stdout.write(str(ans) + '\n')
