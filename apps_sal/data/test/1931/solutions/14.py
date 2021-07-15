for i in range(int(input())):
    n = int(input())
    c = 0
    while n > 1:
        l = 0
        r = 1000000
        while r - l != 1:
            s = (l + r) // 2
            if s*(3*s + 1) // 2 > n:
                r = s
            else:
                l = s
        c += 1
        n -= l*(3*l + 1) // 2
    print(c)

