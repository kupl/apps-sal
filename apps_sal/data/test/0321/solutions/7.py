def check(a):
    for i in range(2, round(a ** 0.5 + 1)):
        if not a % i:
            return 0
    return 1


for i in range(int(input())):
    (a, b) = map(int, input().split())
    if a - b > 1 and a + b > 1:
        print('NO')
    else:
        print('YES' if check(a ** 2 - b ** 2) else 'NO')
