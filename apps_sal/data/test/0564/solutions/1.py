n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
if sum(a) - max(a) <= m:
    print('YES')
else:
    print('NO')
