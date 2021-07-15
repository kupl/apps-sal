n = int(input())

cur = 0
flag = False
for i in range(n):
    t, d = input().split()
    t = int(t)

    if d == 'North':
        flag |= cur < t
        cur -= t
    elif d == 'South':
        flag |= cur + t > 20000
        cur += t
    else:
        flag |= cur in (0, 20000)

flag |= cur != 0
print('YES' if not flag else 'NO')

