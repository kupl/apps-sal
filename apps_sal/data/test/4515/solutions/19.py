n = int(input())
for i in range(n):
    a, b, c, d = list(map(int, input().split()))
    need = max(a, b, c)
    d -= (need - a)
    d -= (need - b)
    d -= (need - c)
    if d >= 0 and d % 3 == 0:
        print('YES')
    else:
        print('NO')

