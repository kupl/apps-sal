q = int(input())
while q:
    q -= 1
    n = int(input())
    a = 0
    b = 0
    c = 0
    for i in range(n):
        s = input()
        c1 = 0
        c2 = 0
        for i in s:
            if i == '1':
                c1 += 1
            else:
                c2 += 1
        if c1 % 2 and c2 % 2:
            a += 1
        elif c1 % 2 == 0 and c2 % 2 == 0:
            c += 1
        else:
            b += 1
    if a % 2 == 0:
        print(n)
    else:
        if b > 0:
            print(n)
        else:
            print(n - 1)
