def calc(n):
    re = 0
    while n % 5 == 0:
        n = n // 5 * 4
        re += 1
    while n % 3 == 0:
        n = n // 3 * 2
        re += 1
    while n % 2 == 0:
        n = n // 2
        re += 1
    if n == 1:
        return re
    else:
        return -1


Q = int(input())
for _ in range(Q):
    print(calc(int(input())))
