n = int(input())
a = int(input())
b = int(input())
max_1 = 6
max_2 = 6
akrat = 4
pole = [n] * 6
pole[0] += -b
pole[1] += -b
while akrat > 0:
    for i in range(6):
        if pole[i] >= a:
            pole[i] += -a
            akrat += -1
            break
if n in pole:
    max_1 = pole.index(n)
else:
    max_1 = 6
if n >= 2 * b:
    akrat = 4
    pole = [n] * 6
    pole[0] += -2 * b
    while akrat > 0:
        for i in range(6):
            if pole[i] >= a:
                pole[i] += -a
                akrat += -1
                break
    if n in pole:
        max_2 = pole.index(n)
    else:
        max_2 = 6
print(min(max_1, max_2))
