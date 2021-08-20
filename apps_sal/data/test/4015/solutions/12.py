def mp():
    return map(int, input().split())


(n, m) = mp()
if m % n != 0:
    print(-1)
else:
    c = 0
    k = m // n
    while k % 2 == 0:
        k //= 2
        c += 1
    while k % 3 == 0:
        k //= 3
        c += 1
    if k == 1:
        print(c)
    else:
        print(-1)
