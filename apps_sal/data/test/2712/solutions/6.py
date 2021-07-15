import sys
ii = lambda: sys.stdin.readline().strip()
idata = lambda: [int(x) for x in ii().split()]

def solve():
    a, b, c = idata()
    print(max(a, b, c))
    return

for t in range(int(ii())):
    solve()

