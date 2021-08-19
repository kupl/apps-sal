(l, r, k) = [int(x) for x in input().split()]
ans = False
x = 1
while x <= r:
    if l <= x:
        print(x, end=' ')
        ans = True
    x *= k
if not ans:
    print(-1)
