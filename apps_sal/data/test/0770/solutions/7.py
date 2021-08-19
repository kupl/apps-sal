a = int(input())
listx = list(map(int, input().split(' ')))
listx2 = [int(x) for x in range(a) if listx[x] == 1]
listx3 = [listx2[x] - listx2[x - 1] - 1 for x in range(1, len(listx2))]
if listx2 == []:
    print(0)
else:
    total = 1
    for i in listx3:
        if i == 0:
            total += 1
        else:
            total += 2
    print(total)
