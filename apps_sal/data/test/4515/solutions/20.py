for _ in range(int(input())):
    (a, b, c, n) = list(map(int, input().split()))
    s = a + b + c + n
    if s % 3 == 0 and s // 3 >= a and (s // 3 >= b) and (s // 3 >= c):
        print('YES')
    else:
        print('NO')
