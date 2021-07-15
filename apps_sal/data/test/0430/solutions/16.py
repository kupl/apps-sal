n = int(input())
a = sorted([int(x) for x in input().split()], reverse=True)
b1 = 0
b2 = 0
for i in a:
    if b1 >= b2:
        b2 += i
    else:
        b1 += i
if b1 == b2:
    print('YES')
else:
    print('NO')

