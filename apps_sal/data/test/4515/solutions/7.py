t = int(input())
while t:
    t -= 1
    (a, b, c, n) = list(map(int, input().split()))
    d = max(a, b, c)
    f = d - a + (d - b) + (d - c)
    if f > n:
        print('NO')
        continue
    n -= f
    if n % 3 == 0:
        print('YES')
    else:
        print('NO')
