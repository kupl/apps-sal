n = int(input())

foc = 1

for i in range(n):
    a = int(input())
    if (a % 2 == 0):
        print(a // 2)
    else:
        if foc == 1:
            print(a // 2 + 1)
        else:
            print(a // 2)
        foc ^= 1

