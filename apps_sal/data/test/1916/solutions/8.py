(n, m) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = 0
for i in range(0, 513):
    c = 1
    for j in a:
        u = 0
        for k in b:
            if i | j & k == i:
                u = 1
                break
        if u == 0:
            c = 0
            break
    if c == 1:
        print(i)
        break
