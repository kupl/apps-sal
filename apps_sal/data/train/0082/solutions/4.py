import sys
ii = lambda: sys.stdin.readline().strip()
idata = lambda: [int(x) for x in ii().split()]

def solve():
    n = int(ii())
    data = idata()
    print(*data[::-1])
    return

for t in range(int(ii())):
    solve()

