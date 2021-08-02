x, y, z = list(map(int, input().split()))
a, b, c = list(map(int, input().split()))
flag = 0
if(a < x):
    print('NO')
    return
a -= x
if(a + b < y):
    print('NO')
    return
if(a + b + c - y < z):
    print('NO')
    return
print('YES')
