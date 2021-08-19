for tt in range(int(input())):
    (n, m) = map(int, input().split())
    if n == 1 or m == 1 or (n == 2 and m == 2):
        print('YES')
        continue
    print('NO')
