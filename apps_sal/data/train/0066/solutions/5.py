import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    print(*a)
    print(*b)

t = int(input())
for i in range(t):
    solve()


