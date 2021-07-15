n, t = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
now = 0
result = 0
while now < n - 1:
    now += a[now]
    if now + 1 == t:
        result = 1
if result:
    print('YES')
else:
    print('NO')
