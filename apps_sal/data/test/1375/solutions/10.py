ints = int(input())
listx = list(map(int, input().split(' ')))
sumx = sum(listx)
if sumx % 3 != 0:
    print(0)
else:
    num1 = 0
    num2 = 0
    ctotal = 0
    listx.reverse()
    listx.remove(listx[0])
    listx.reverse()
    for i in listx:
        ctotal += i
        if ctotal == int(sumx * 2 / 3):
            num2 += num1
        if ctotal == int(sumx * 1 / 3):
            num1 += 1
    print(num2)
