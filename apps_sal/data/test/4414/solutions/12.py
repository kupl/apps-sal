n = int(input())
for _ in range(n):
    a, b, n, s = map(int, input().split())
    t = min(s // n, a)
    if b >= s - t * n:
        print('YES')
    else:
        print('NO')
