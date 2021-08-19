(a, b, c) = [int(i) for i in input().split()]
if a < b and c <= 0 or (a > b and c >= 0):
    print('NO')
elif a == b:
    print('YES')
elif c == 0:
    print('NO')
elif (b - a) % c == 0:
    print('YES')
else:
    print('NO')
