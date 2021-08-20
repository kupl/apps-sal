import os
import sys
if os.path.exists('/mnt/c/Users/Square/square/codeforces'):
    f = iter(open('A.txt').readlines())

    def input():
        return next(f)
else:

    def input():
        return sys.stdin.readline().strip()
fprint = lambda *args: print(*args, flush=True)


def min_max(x):
    l = list(str(x))
    return (int(min(l)), int(max(l)))


t = int(input())
for _ in range(t):
    (a, K) = map(int, input().split())
    K -= 1
    for _ in range(K):
        (u, v) = min_max(a)
        if u == 0:
            break
        a += u * v
    print(a)
