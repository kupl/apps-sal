t = int(input())
for fk in range(t):
    (n, m) = [int(x) for x in input().split()]
    if n == 1 or m == 1:
        print('YES')
    elif n == 2 and m == 2:
        print('YES')
    else:
        print('NO')
