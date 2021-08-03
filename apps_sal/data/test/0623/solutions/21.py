ch = input()
d = ch.split()
a1 = int(d[0])
a2 = int(d[1])
somme = 0
while a1 > 0 and a2 > 0:
    if a1 >= a2:
        if a1 % 2 == 0:
            S = a1 // 2 - 1
            a1 = a1 - S * 2
            a2 = a2 + S
            somme += S

        else:
            S = a1 // 2
            a1 -= S * 2
            a2 = a2 + S
            somme += S

    else:
        if a2 % 2 == 0:
            S = a2 // 2 - 1
            a2 -= S * 2
            a1 = a1 + S
            somme += S

        else:
            S = a2 // 2
            a2 -= S * 2
            a1 = a1 + S
            somme += S

    if (a1 == 2 and a2 == 2) or (a1 < 2 and a2 == 2) or (a2 < 2 and a1 == 2):
        somme = somme + 1
        break
    if a1 < 2 and a2 < 2:
        break

print(somme)
