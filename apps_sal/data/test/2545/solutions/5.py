n = int(input())
for i in range(n):
    (a, b) = tuple(map(int, input().split()))
    (a, b) = (min(a, b), max(a, b))
    if (a + b) % 3 == 0 and a >= b - a:
        print('YES')
    else:
        print('NO')
