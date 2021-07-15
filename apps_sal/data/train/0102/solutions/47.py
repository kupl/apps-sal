t = int(input())
for i in range(t):
    n = int(input())
    l = len(str(n))
    c = 0
    for j in range(1, 10):
        g = 10
        num = j
        for d in range(1, 11):
            if num <= n:
                c += 1
                num += g * j
                g *= 10

    print(c)



