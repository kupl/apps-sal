t = int(input())
for i10 in range(t):
    (n, m) = list(map(int, input().split()))
    if n == 1 or m == 1 or n + m == 4:
        print('YES')
    else:
        print('NO')
