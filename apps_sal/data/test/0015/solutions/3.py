(a, b, c) = list(map(int, input().split()))
if c == 0 and b == a:
    print('YES')
elif c == 0:
    print('NO')
elif (b - a) % c == 0 and (c >= 0 and b >= a or (c <= 0 and b <= a)):
    print('YES')
else:
    print('NO')
