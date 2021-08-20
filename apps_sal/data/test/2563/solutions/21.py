for _ in range(int(input())):
    long = list(map(int, list(input())))
    odd = []
    even = []
    for n in long:
        if n % 2 == 1:
            odd.append(n)
        else:
            even.append(n)
    even.append(10)
    odd.append(11)
    i1 = 0
    i2 = 0
    for i in range(len(long)):
        if even[i1] < odd[i2]:
            print(even[i1], end='')
            i1 += 1
        else:
            print(odd[i2], end='')
            i2 += 1
    print()
