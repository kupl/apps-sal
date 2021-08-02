import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    yasser = sum(a)
    ans = True
    cur = 0
    for i in range(n - 1):
        cur += a[i]
        if cur <= 0:
            ans = False
            break
    cur = 0
    for i in reversed(list(range(1, n))):
        cur += a[i]
        if cur <= 0:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")


t = int(input())
for i in range(t):
    solve()
