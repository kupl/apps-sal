n = int(input())
for i in range(n):
    t = int(input())
    c = 0
    for r in range(1, 10):
        for k in range(1, 11):
            if int(str(r) * k) <= t:
                c += 1
    print(c)
