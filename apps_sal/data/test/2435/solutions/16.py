def solve():
    n, x, m = map(int, input().split())
    al, ar = x, x
    for i in range(m):
        l, r = map(int, input().split())
        if max(l, al) <= min(r, ar):
            al = min(al, l)
            ar = max(ar, r)
    print(ar - al + 1)


t = int(input())
for _ in range(t):
    solve()
