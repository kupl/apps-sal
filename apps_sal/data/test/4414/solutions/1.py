for __ in range(int(input())):
    a, b, n, s = list(map(int, input().split()))
    x = s % n
    if x > b or a * n + b < s:
        print('NO')
    else:
        print('YES')
