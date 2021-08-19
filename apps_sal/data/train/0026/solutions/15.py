t = int(input())
for case in range(t):
    (n, m) = list(map(int, input().split()))
    if min(n, m) == 1:
        print('YES')
    elif n == m and n == 2:
        print('YES')
    else:
        print('NO')
