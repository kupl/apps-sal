for i in range(int(input())):
    n = int(input())
    a = 0
    b = 0
    for j in range(int(n / 2)):
        a += 2**(j + 1)
        b += 2**(j + 2)
    print(int(b - a))
