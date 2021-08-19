n = int(input())
twoes = [0]
fives = [0]
if n % 2 == 1:
    print(0)
else:
    i = 0
    while 1:
        if n // 2 ** (i + 1) != 0:
            twoes.append(n // 2 ** (i + 1))
            i += 1
        else:
            break
    i = 0
    while 1:
        temp5 = n // 5 ** (i + 1) // 2
        if temp5 != 0:
            fives.append(temp5)
            i += 1
        else:
            break
    print(min(sum(twoes), sum(fives)))
