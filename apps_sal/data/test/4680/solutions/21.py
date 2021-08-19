(a, b, c) = map(int, input().split())
if a == 5:
    if b == 5 and c == 7 or (b == 7 and c == 5):
        print('YES')
    else:
        print('NO')
elif a == 7 and b == c == 5:
    print('YES')
else:
    print('NO')
