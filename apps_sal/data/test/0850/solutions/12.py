a = int(input())
mas = input().split()
count1 = 0
count2 = True
Zero = Hungred = Ten = Remain = True
mas2 = []
mas3 = []
final = []
for i in range(len(mas)):
    mas[i] = int(mas[i])
if a == 1:
    print(1)
    print(*mas)
else:
    for i in range(len(mas)):
        if mas[i] == 100 and Hungred:
            Hungred = False
            final.append(mas[i])
        elif mas[i] == 0 and Zero:
            Zero = False
            final.append(mas[i])
        elif (mas[i] % 10 == 0) & Ten:
            Ten = False
            final.append(mas[i])
        elif (mas[i] < 10 != 0) & Remain:
            Remain = False
            final.append(mas[i])
    if Ten == Remain == True:
        for i in range(len(mas)):
            if mas[i] != 100 and mas[i] != 0:
                final.append(mas[i])
                break
        print(len(final))
        print(*final)
    else:
        print(len(final))
        print(*final)
