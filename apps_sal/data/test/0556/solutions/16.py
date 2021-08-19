(l, r, k) = map(int, input().split())
cur = 1
while cur < l:
    cur *= k
f = False
while cur <= r:
    f = True
    print(cur, end=' ')
    cur *= k
if not f:
    print(-1)
