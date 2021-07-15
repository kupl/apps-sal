import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def solve():
    n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = min(sum(a), m)
    print(ans)

t = int(input())
for i in range(t):
    solve()

