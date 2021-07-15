def main():
    str1 = input()
    str2 = input()
    poz_real = 0
    for i in range(len(str1)):
        if str1[i] == '+':
            poz_real += 1
        else:
            poz_real -= 1
    poz = [0]
    lent = 1
    for i in range(len(str2)):
        if str2[i] == '+':
            for j in range(len(poz)):
                poz[j] += 1
        if str2[i] == '-':
            for j in range(len(poz)):
                poz[j] -= 1
        if str2[i] == '?':
            for j in range(len(poz) - int(lent), len(poz)):
                poz.append(poz[j] - 1)
                poz.append(poz[j] + 1)
            lent *= 2
    count_sovp = 0
    was = []
    for i in range(len(poz) - int(lent), len(poz)):
        if poz[i] == poz_real:
            count_sovp += 1
    print(float(count_sovp/lent))

def __starting_point():
    main()

__starting_point()
