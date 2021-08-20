t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if sum(a) == m:
        print('YES')
    else:
        print('NO')
