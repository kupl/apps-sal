n = int(input())
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if a == 2:
        a = 3
    if a >= 4:
        print('YES')
    elif a >= b:
        print('YES')
    else:
        print('NO')
