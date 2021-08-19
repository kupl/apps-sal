(n, d) = list(map(int, input().split()))
N = int(input())
for i in range(N):
    (x, y) = list(map(int, input().split()))
    if x + y >= d and x + y <= n + n - d and (x + y >= d) and (abs(x - y) <= d):
        print('YES')
    else:
        print('NO')
