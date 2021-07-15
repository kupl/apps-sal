n, m = map(int,input().split())
d = m // n
ans = 0
p = 1
while d % 3 == 0:
    ans += 1
    d //= 3
    p *= 3
while d % 2 == 0:
    ans += 1
    d //= 2
    p *= 2
if d != 1 or p*n != m:
    print(-1)
else:
    print(ans)
