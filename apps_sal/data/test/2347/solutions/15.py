import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def solve():
    p = sorted(input())
    h = input()
    n = len(p)
    m = len(h)
    if n > m:
        print("NO")
        return
    for i in range(m - n + 1):
        if sorted(h[i:i + n]) == p:
            print("YES")
            return
    print("NO")


t = int(input())
for i in range(t):
    solve()
