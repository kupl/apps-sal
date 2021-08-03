n = int(input())

fives = [0]

if n % 2 == 1:
    print(0)
else:
    i = 0
    while 1:
        temp5 = (n // (5 ** (i + 1))) // 2
        if temp5 != 0:
            fives.append(temp5)
            i += 1
        else:
            break
    print(sum(fives))
