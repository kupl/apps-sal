oishisa = list(map(int, input().split()))

souwa = sum(oishisa)

for i in range(2**4):
    wa = 0
    for j in range(4):
        if ((i >> j) & 1):
            wa += oishisa[j]

    if wa == souwa / 2:
        print('Yes')
        break

    if i == 15:
        print('No')
