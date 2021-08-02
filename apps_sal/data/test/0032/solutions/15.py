n = int(input())
x = 0
ans = True

for i in range(n):
    t, d = input().split()
    t = int(t)
    if d == 'South' and x + t > 20000:
        ans = False
    elif d == 'North' and x - t < 0:
        ans = False
    elif (d == 'West' or d == 'East') and (x == 0 or x == 20000):
        ans = False
    if d == 'South':
        x += t
    elif d == 'North':
        x -= t

if x != 0:
    ans = False

if ans:
    print('YES')
else:
    print('NO')
