def solvable(la):
    colors_faces = [set() for _ in range(6)]
    for (i, a) in zip(list(range(50)), la):
        face = i // 4
        colors_faces[face].add(a)
        if len(colors_faces[face]) > 2:
            return False
    ones = []
    twos = []
    for (i, face_set) in enumerate(colors_faces):
        if len(face_set) == 1:
            ones.append(i)
        else:
            twos.append(i)
    twos.sort()
    possibilities = [[0, 1, 2, 5], [0, 2, 3, 4], [1, 3, 4, 5]]
    if twos not in possibilities:
        return False
    yep = False
    if twos == [0, 1, 2, 5]:
        yep = la[0] == la[2] and la[2] == la[5] and (la[5] == la[7]) and (la[1] == la[3]) and (la[3] == la[21]) and (la[21] == la[23]) and (la[4] == la[6]) and (la[6] == la[9]) and (la[9] == la[11]) and (la[8] == la[10]) and (la[10] == la[20]) and (la[20] == la[22]) or (la[0] == la[2] and la[2] == la[20] and (la[20] == la[22]) and (la[1] == la[3]) and (la[3] == la[4]) and (la[4] == la[6]) and (la[5] == la[7]) and (la[7] == la[8]) and (la[8] == la[10]) and (la[9] == la[11]) and (la[11] == la[21]) and (la[21] == la[23]))
    elif twos == [0, 2, 3, 4]:
        yep = la[0] == la[1] and la[1] == la[16] and (la[16] == la[18]) and (la[17] == la[19]) and (la[19] == la[9]) and (la[9] == la[8]) and (la[10] == la[11]) and (la[11] == la[15]) and (la[15] == la[13]) and (la[2] == la[3]) and (la[3] == la[12]) and (la[12] == la[14]) or (la[0] == la[1] and la[1] == la[13] and (la[13] == la[15]) and (la[2] == la[3]) and (la[3] == la[17]) and (la[17] == la[19]) and (la[12] == la[14]) and (la[14] == la[8]) and (la[8] == la[9]) and (la[10] == la[11]) and (la[11] == la[16]) and (la[16] == la[18]))
    elif twos == [1, 3, 4, 5]:
        yep = la[12] == la[13] and la[13] == la[6] and (la[6] == la[7]) and (la[4] == la[5]) and (la[5] == la[18]) and (la[18] == la[19]) and (la[16] == la[17]) and (la[17] == la[22]) and (la[22] == la[23]) and (la[20] == la[21]) and (la[21] == la[14]) and (la[14] == la[15]) or (la[14] == la[15] and la[4] == la[5] and (la[14] == la[4]) and (la[6] == la[7]) and (la[6] == la[16]) and (la[16] == la[17]) and (la[18] == la[19]) and (la[19] == la[20]) and (la[20] == la[21]) and (la[12] == la[13]) and (la[13] == la[22]) and (la[22] == la[23]))
    return yep


la = list(map(int, input().split()))
print('YES' if solvable(la) else 'NO')
