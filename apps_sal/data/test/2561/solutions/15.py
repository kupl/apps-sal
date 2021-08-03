t = int(input())
for i in range(t):
    s = 0
    a = int(input())
    while a != 0:
        if a % 2 == 1:
            s += 1
        a = a // 2
    print(2**s)
