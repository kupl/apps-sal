(n, k) = [int(v) for v in input().split()]
if k == 1:
    print(n)
else:
    nn = n
    p = 0
    while nn:
        nn //= 2
        p += 1
    print(2 ** p - 1)
