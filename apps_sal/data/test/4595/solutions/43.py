retu = input()
kari = 0
flag = False
for i in range(len(retu)):
    if flag:
        kari += 1
        if retu[i] == 'Z':
            an = kari
    elif retu[i] == 'A':
        flag = True
        kari += 1
print(an)
