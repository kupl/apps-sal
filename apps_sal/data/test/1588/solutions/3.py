def __starting_point():
    n = int(input())
    l = [int(i) for i in list(input().split())]
    size = 10 ** 6
    mask = [0] * (size + 1)
    for i in l:
        mask[i] = 1
    counter = 0
    result = []
    for i in range(1, size + 1):
        if mask[i] == 1 and mask[size + 1 - i] == 0:
            mask[size + 1 - i] = 2
            result.append(size + 1 - i)
        elif mask[i] == 1 and mask[size + 1 - i] == 1:
            counter += 1
            mask[size + 1 - i] = 2
        elif mask[i] == 0 and mask[size + 1 - i] == 0 and (counter > 0):
            mask[i] = 2
            mask[size + 1 - i] = 2
            result.append(i)
            result.append(size + 1 - i)
            counter -= 1
    print(len(result))
    print(*result)


__starting_point()
