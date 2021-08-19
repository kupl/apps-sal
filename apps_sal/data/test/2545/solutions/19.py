t = int(input())
for kkk in range(t):
    (a, b) = map(int, input().split())
    if a > 2 * b or b > 2 * a:
        print('NO')
    elif a == 0 and b == 0:
        print('YES')
    elif a == 0 or b == 0:
        print('NO')
    elif (a + b) % 3 == 0:
        print('YES')
    else:
        print('NO')
