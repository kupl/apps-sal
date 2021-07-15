q = int(input())
for i in range(q):
    n = int(input())
    prod = 1
    prods = [1]
    sum1 = 0
    a = []
    while prod < n:
        sum1 += prod
        a.append(1)
        prod *= 3
        prods.append(prod)
    if sum1 < n:
        print(prod)
    else:
        for i in range(len(prods) - 1, -1, -1):
            if sum1 - prods[i] >= n:
                sum1 -= prods[i]
        print(sum1)
