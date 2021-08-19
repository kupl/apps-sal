cubecount = input()
cubies = []
for i in range(int(cubecount)):
    cubies.append(input().split(' '))
count = 0
while count < 1000:
    p = False
    candidate = str(count + 1)
    if count + 1 < 10:
        for cube in cubies:
            if candidate in cube:
                p = True
    elif count + 1 < 100:
        for cube in cubies:
            if candidate[0] in cube:
                cubieb = cubies.copy()
                cubieb.remove(cube)
                for cubeb in cubieb:
                    if candidate[1] in cubeb:
                        p = True
    else:
        for cube in cubies:
            if candidate[0] in cube:
                cubieb = cubies.copy()
                cubieb.remove(cube)
                for cubeb in cubieb:
                    if candidate[1] in cubeb:
                        cubiec = cubieb.copy()
                        cubiec.remove(cubeb)
                        for cubec in cubiec:
                            if candidate[2] in cubec:
                                p = True
    if p:
        count += 1
    else:
        break
print(count)
