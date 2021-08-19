(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
if n - 1 + sum(a) == x:
    print('YES')
else:
    print('NO')
