for _ in range(int(input())):
    a, b, n, s = map(int, input().split())
    maxi = n * a
    rem = s % n
    z = s // n * n
    z = min(z, a * n)
    if s - z <= b:
        print('YES')
    else:
        print('NO')
