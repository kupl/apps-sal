n = int(input())
listNum = sorted(list(map(int, input().split())))
setNum = set(listNum)
powTwo = list([2**x for x in (list(range(0, 32)))])
found2 = False
found3 = False
res = [0, 0, 0]
for powNum in powTwo:
    for num in listNum:
        if (found3):
            break
        if (num + powNum) in setNum:
            found2 = True
            if (found3 == False):
                res[0] = num
                res[1] = num + powNum
            if num + 2 * powNum in setNum:
                found3 = True
                res[0] = num
                res[1] = num + powNum
                res[2] = num + 2 * powNum
if (found3):
    print(3)
    print(res[0], res[1], res[2])
elif (found2):
    print(2)
    print(res[0], res[1])
else:
    print(1)
    print(listNum[0])
