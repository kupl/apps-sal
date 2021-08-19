n = int(input())
f = True
a = 1
b = 2
for i in range(n):
    k = int(input())
    if k != a and k != b:
        f = False
    l = [a, b]
    if 1 not in l:
        b = 1
    elif 2 not in l:
        b = 2
    else:
        b = 3
    a = k
    if k == b:
        f = False
if f:
    print('YES')
else:
    print('NO')
