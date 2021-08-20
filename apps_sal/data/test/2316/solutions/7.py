t = int(input())
for g in range(t):
    (x, a, b) = list(map(int, input().split()))
    while x > 20 and a > 0:
        x = x // 2 + 10
        a -= 1
    x -= 10 * b
    if x > 0:
        print('NO')
    else:
        print('YES')
