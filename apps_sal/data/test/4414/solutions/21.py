q = int(input())
for i in range(q):
    (a, b, c, d) = map(int, input().split())
    if a * c > d:
        d %= c
    else:
        d -= a * c
    print('YES' if d <= b else 'NO')
