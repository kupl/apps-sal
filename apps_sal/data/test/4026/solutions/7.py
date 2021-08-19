t = int(input())
for j in range(t):
    (n, m) = list(map(int, input().split()))
    bol = False
    for i in range(n):
        (a, b) = list(map(int, input().split()))
        (c, d) = list(map(int, input().split()))
        if b == c:
            bol = True
    if m % 2 == 0 and bol:
        print('YES')
    else:
        print('NO')
