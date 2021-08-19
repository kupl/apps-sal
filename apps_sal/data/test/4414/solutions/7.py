q = int(input())
for i in range(q):
    (a, b, n, S) = map(int, input().split())
    if a * n >= S:
        x = S // n
    else:
        x = a
    if b >= S - x * n:
        print('YES')
    else:
        print('NO')
