f = list(map(int, input().split()))
f.sort()
a = f[0]
b = f[1]
c = f[2]
if a == 1:
    print('YES')
elif a == 3 and b == 3 and (c == 3):
    print('YES')
elif a != 2:
    print('NO')
elif b == 2 or (b == 4 and c == 4):
    print('YES')
else:
    print('NO')
