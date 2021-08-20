def stones():
    datain = []
    removed = 0
    for i in range(2):
        datain.append(input())
    colors = datain[1]
    for i in range(len(colors)):
        if i == len(colors) - 1:
            break
        elif colors[i] == colors[i + 1]:
            removed += 1
    print(removed)


stones()
