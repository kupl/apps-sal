q = int(input())
for iqwwq in range(q):
    n = int(input())
    sp = input().split()
    k0, k1, k2 = 0, 0, 0
    for i in sp:
        if int(i) % 3 == 0:
            k0 += 1
        elif int(i) % 3 == 1:
            k1 += 1
        else:
            k2 += 1
    if k2 > k1:
        k2 -= k1
        print(k0 + k1 + (k2 // 3))
    else:
        k1 -= k2
        print(k0 + (k1 // 3) + k2)
