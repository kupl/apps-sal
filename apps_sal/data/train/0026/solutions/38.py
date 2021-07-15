for _ in range(int(input())):
    n, m = map(int, input().split())
    print('YES' if n == 1 or m == 1 or (n == 2 and m == 2) else 'NO')
