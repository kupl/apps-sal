pocet = int(input())
pole = list(map(int, input().split()))
pole.sort()
(boolean, pole2) = (True, [])
for i in range(len(pole)):
    if boolean:
        pole2.append(str(pole[i // 2]))
    else:
        pole2.append(str(pole[-(i // 2 + 1)]))
    boolean = not boolean
print(' '.join(pole2))
