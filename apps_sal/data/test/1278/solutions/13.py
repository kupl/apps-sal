ints = [int(x) for x in input().split()]
days = [int(x) for x in input().split()]
for i in range(ints[0]):
    pos = True
    for j in range(min(ints[1], i)):
        if days[i - j - 1] < days[i]:
            pos = False
            break
    for k in range(min(ints[2], ints[0] - i - 1)):
        if days[i + k + 1] < days[i]:
            pos = False
            break
    if pos == True:
        print(i + 1)
        break
