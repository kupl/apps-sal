some = input().split(' ')
n = int(some[0])
m = int(some[1])
y = 0
for i in range(n):
    some = input().split(' ')
    a = int(some[0])
    b = int(some[1])
    if y >= a:
        y = max(y, b)
if y >= m:
    print('YES')
else:
    print('NO')
