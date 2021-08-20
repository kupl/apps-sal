for case in range(int(input())):
    (a, b) = [int(x) for x in input().split()]
    s = 0
    while a * 8 <= b:
        a *= 8
        s += 1
    while a * 4 <= b:
        a *= 4
        s += 1
    while a * 2 <= b:
        a *= 2
        s += 1
    while a % 8 == 0 and a // 8 >= b:
        a //= 8
        s += 1
    while a % 4 == 0 and a // 4 >= b:
        a //= 4
        s += 1
    while a % 2 == 0 and a // 2 >= b:
        a //= 2
        s += 1
    if a == b:
        print(s)
    else:
        print(-1)
