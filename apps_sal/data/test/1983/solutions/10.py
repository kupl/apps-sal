import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = len(set(a))
    print(ans)


t = int(input())
for i in range(t):
    solve()
