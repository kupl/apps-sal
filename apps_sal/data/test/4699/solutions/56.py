n, k = [int(x) for x in input().split()]
ds = {int(x) for x in input().split()}
ns = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - ds
temp = 0
d = {}
a = 1
b = {}
m = len(str(n)) + 1
over = False
while(a <= m and not over):
    c = []
    d = 10**(a - 1)
    for v in ns:
        if a > 1:
            for bv in b[a - 1]:
                t = v * d + bv
                c += [t]
                if t >= n:
                    print(t)
                    over = True
                    break
            if over:
                break
        else:
            t = v * d
            c += [t]
            if t >= n:
                print(t)
                over = True
                break

    b[a] = c
    a += 1
