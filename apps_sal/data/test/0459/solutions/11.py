line = list(map(int, input().split()))
yes = False
q = [1, -1]
if line[4] == line[5] and line[5] == line[6] and (line[6] == line[7]):
    if line[20] == line[21] and line[21] == line[22] and (line[22] == line[23]):
        can = True
        c1 = []
        if line[15] != line[13]:
            can = False
        else:
            c1 += [line[15]]
        if line[3] != line[2]:
            can = False
        else:
            c1 += [line[3]]
        if line[16] != line[18]:
            can = False
        else:
            c1 += [line[16]]
        if line[8] != line[9]:
            can = False
        else:
            c1 += [line[8]]
        c2 = []
        if line[12] != line[14]:
            can = False
        else:
            c2 += [line[14]]
        if line[0] != line[1]:
            can = False
        else:
            c2 += [line[1]]
        if line[17] != line[19]:
            can = False
        else:
            c2 += [line[19]]
        if line[10] != line[11]:
            can = False
        else:
            c2 += [line[11]]
        if can:
            for i in range(2):
                c3 = []
                for j in range(4):
                    c3 += [c1[(q[i] + j) % 4]]
                if c3 == c2:
                    yes = True
if line[0] == line[1] and line[1] == line[2] and (line[2] == line[3]):
    if line[8] == line[9] and line[9] == line[10] and (line[10] == line[11]):
        can = True
        c1 = []
        if line[12] != line[13]:
            can = False
        else:
            c1 += [line[12]]
        if line[4] != line[5]:
            can = False
        else:
            c1 += [line[4]]
        if line[16] != line[17]:
            can = False
        else:
            c1 += [line[16]]
        if line[20] != line[21]:
            can = False
        else:
            c1 += [line[21]]
        c2 = []
        if line[14] != line[15]:
            can = False
        else:
            c2 += [line[14]]
        if line[6] != line[7]:
            can = False
        else:
            c2 += [line[7]]
        if line[18] != line[19]:
            can = False
        else:
            c2 += [line[19]]
        if line[22] != line[23]:
            can = False
        else:
            c2 += [line[23]]
        if can:
            for i in range(2):
                c3 = []
                for j in range(4):
                    c3 += [c1[(q[i] + j) % 4]]
                if c3 == c2:
                    yes = True
if line[12] == line[13] and line[13] == line[14] and (line[14] == line[15]):
    if line[16] == line[17] and line[17] == line[18] and (line[18] == line[19]):
        can = True
        c1 = []
        if line[0] != line[2]:
            can = False
        else:
            c1 += [line[2]]
        if line[4] != line[6]:
            can = False
        else:
            c1 += [line[4]]
        if line[8] != line[10]:
            can = False
        else:
            c1 += [line[10]]
        if line[23] != line[21]:
            can = False
        else:
            c1 += [line[21]]
        c2 = []
        if line[1] != line[3]:
            can = False
        else:
            c2 += [line[1]]
        if line[5] != line[7]:
            can = False
        else:
            c2 += [line[7]]
        if line[11] != line[9]:
            can = False
        else:
            c2 += [line[9]]
        if line[22] != line[20]:
            can = False
        else:
            c2 += [line[20]]
        if can:
            for i in range(2):
                c3 = []
                for j in range(4):
                    c3 += [c1[(q[i] + j) % 4]]
                if c3 == c2:
                    yes = True
if yes:
    print('YES')
else:
    print('NO')
