def Y(f):
    if f:
        print('YES')
    else:
        print('NO')


n = int(input())
for _ in range(n):
    (a, b) = map(int, input().split())
    if a == 1:
        Y(b == 1)
    elif a <= 3:
        Y(b <= 3)
    else:
        Y(1)
