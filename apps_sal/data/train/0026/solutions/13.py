for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    print('YES' if min(n, m) == 1 or max(n, m) <= 2 else 'NO')
