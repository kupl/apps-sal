n = int(input())
a = []
if n == 1 or n == 2:
    print(1)
    print(1)
elif n == 3:
    print(2)
    print(1, 3)
elif n == 4:
    print(4)
    print(3, 1, 4, 2)
else:
    if n % 2 != 0:
        ind1 = n // 2 + 2
    else:
        ind1 = n // 2 + 1
    ind2 = 1
    for i in range(n):
        if i % 2 == 0:
            a.append(ind2)
            ind2 += 1
        else:
            a.append(ind1)
            ind1 += 1
    print(n)
    print(*a)
