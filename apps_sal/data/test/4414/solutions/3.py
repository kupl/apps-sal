Q = int(input())
for _ in range(Q):
    (a, b, n, S) = list(map(int, input().split()))
    left = S - min(a, S // n) * n
    if left <= b:
        print('YES')
    else:
        print('NO')
