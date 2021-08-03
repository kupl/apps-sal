n, m = map(int, input().strip().split())
can = True
if m % n != 0:
    can = False
k = m / n
ans = 0
while k % 2 == 0:
    k = k / 2
    ans += 1
while k % 3 == 0:
    k = k / 3
    ans += 1
if k != 1:
    can = False
if can:
    print(ans)
else:
    print(-1)
