u, v = list(map(int, input().split()))
if u > v:
    print(-1)
elif u == v:
    if u == v == 0:
        print(0)
    else:
        print(1)
        print(u)
elif (v - u) % 2 == 1:
    print(-1)
else:
    a = u
    b = 0
    for i in reversed(list(range(65))):
        res = v - (a + b)
        if u & (1 << i):
            continue
        if res >= 2 * (1 << i):
            a += 1 << i
            b += 1 << i
        else:
            continue
    if a + b == v:
        print(2)
        print(a, b)
    else:
        print(3)
        k = (v - u) // 2
        print(u, k, k)
