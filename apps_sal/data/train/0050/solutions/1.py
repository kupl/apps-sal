import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    red = a.count(1)
    blue = 2*n - red
    s = red-blue
    if s == 0:
        print(0)
        return

    cur = 0
    d = {0:0}
    for i in range(n, 2*n):
        if a[i] == 2:
            cur -= 1
        else:
            cur += 1
        if cur not in d:
            d[cur] = i-n+1
    ans = float("inf")
    need = s
    cur = 0
    if need in d:
        ans = min(ans, d[need])
    for i in reversed(list(range(n))):
        if a[i] == 2:
            cur -= 1
        else:
            cur += 1
        if need-cur in d:
            ans = min(ans, d[need-cur]+n-i)
    print(ans)

t = int(input())
for i in range(t):
    solve()


