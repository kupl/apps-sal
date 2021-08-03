n = int(input())
c = 0
while n > 0:
    n -= 1
    a = int(input())
    if a % 2 == 0:
        print(a // 2)
        c -= 1
    elif c % 2 == 1:
        print(a // 2)
    else:
        print(a // 2 + 1)
    c += 1
