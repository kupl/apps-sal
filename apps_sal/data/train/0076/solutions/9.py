import sys

def ii():
    return sys.stdin.readline().strip()

def idata():
    return [int(x) for x in ii().split()]

def solve():
    n = int(ii())
    if n % 4 == 0:
        print('YES')
    else:
        print('NO')
    return

for t in range(int(ii())):
    solve()

