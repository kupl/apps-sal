(n, k) = list(map(int, input().split()))
t = n // k
if t % 2 == 1:
    print('YES')
else:
    print('NO')
