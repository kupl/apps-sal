k, p = int(input()), list(map(float, input().split()))
p.sort(reverse = True)
if p[0] == 1: print(1)
else:
    a = 1
    b = v = 0
    for i in p:
        a *= 1 - i
        b += i / (1 - i)
        u = a * b
        if v > u: break
        v = u
    print(v)
