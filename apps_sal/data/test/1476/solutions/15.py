
n = int(input())

if n == 1:
    print(1)
    print(1)
elif n == 2:
    print(1)
    print(2)
elif n == 3:
    print(2)
    print(*[1, 3])
elif n == 4:
    print(4)
    print(*[3, 1, 4, 2])
else:

    L = [0] * n

    i = 0
    j = 1
    while j <= n:
        L[i] = j
        j += 2
        i += 1

    j = 2
    while j <= n:
        L[i] = j
        i += 1
        j += 2

    print(len(L))
    print(*L)
