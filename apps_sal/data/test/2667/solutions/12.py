n = int(input())
stamps = list(map(int, input().split()))
if sum(stamps) == n * (n + 1) / 2:
    print('YES')
else:
    print('NO')
