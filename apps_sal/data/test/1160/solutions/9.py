TShirts = list(map(int, input().split()))
NPers = int(input())
Needs = [0,0,0,0,0]
T = [0 for i in range(10)]
Pers = []
IsFound = True

if sum(TShirts) < NPers:
    IsFound = False

for i in range(NPers):
    s = input().split(',')
    Pers.append(0)
    if 'S' in s:
        Pers[-1] += 1
    if 'M' in s:
        Pers[-1] += 2
    if 'L' in s:
        Pers[-1] += 4
    if 'XL' in s:
        Pers[-1] += 8
    if 'XXL' in s:
        Pers[-1] += 16
    if 'XXXL' in s:
        Pers[-1] += 32

for i in Pers:
    if i==1 :
        TShirts[0] -= 1
    elif i==2 :
        TShirts[1] -= 1
    elif i==4 :
        TShirts[2] -= 1
    elif i==8 :
        TShirts[3] -= 1
    elif i==16 :
        TShirts[4] -= 1
    elif i==32 :
        TShirts[5] -= 1

for i in TShirts:
    if i < 0 and IsFound:
        IsFound = False

for i in Pers:
    if (i&1!=0) and (i&2!=0):
        Needs[0] += 1
    elif (i & 2!=0) and (i & 4!=0):
        Needs[1] += 1
    elif (i & 4!=0) and (i & 8!=0):
        Needs[2] += 1
    elif (i & 8!=0) and (i & 16!=0):
        Needs[3] += 1
    elif (i & 16!=0) and (i & 32!=0):
        Needs[4] += 1


for i in range(5):
    while Needs[i] > 0 and TShirts[i]>0:
        Needs[i] -= 1
        TShirts[i] -= 1
        T[2*i] += 1
    while Needs[i] > 0 and TShirts[i+1] > 0:
        Needs[i] -= 1
        TShirts[i+1] -= 1
        T[2*i + 1] += 1

if sum(Needs) > 0:
    IsFound = False

if IsFound:
    print('YES')

    for i in range(len(Pers)):
        if T[0] > 0 and Pers[i] == 3:
            Pers[i] -= Pers[i] - 1
            T[0] -= 1
        elif T[1] > 0 and Pers[i] == 3:
            Pers[i] -= Pers[i] - 2
            T[1] -= 1
    for i in range(len(Pers)):
        if T[2] > 0 and Pers[i] == 6:
            Pers[i] -= Pers[i] - 2
            T[2] -= 1
        elif T[3] > 0 and Pers[i] == 6:
            Pers[i] -= Pers[i] - 4
            T[3] -= 1
    for i in range(len(Pers)):
        if T[4] > 0 and Pers[i] == 12:
            Pers[i] -= Pers[i] - 4
            T[4] -= 1
        elif T[5] > 0 and Pers[i] == 12:
            Pers[i] -= Pers[i] - 8
            T[5] -= 1
    for i in range(len(Pers)):
        if T[6] > 0 and Pers[i] == 24:
            Pers[i] -= Pers[i] - 8
            T[6] -= 1
        elif T[7] > 0 and Pers[i] == 24:
            Pers[i] -= Pers[i] - 16
            T[7] -= 1
    for i in range(len(Pers)):
        if T[8] > 0 and Pers[i] == 48:
            Pers[i] -= Pers[i] - 16
            T[8] -= 1
        elif T[9] > 0 and Pers[i] == 48:
            Pers[i] -= Pers[i] - 32
            T[9] -= 1

    for i in Pers:
        if i & 1:
            print('S')
        elif i & 2:
            print('M')
        elif i & 4:
            print('L')
        elif i & 8:
            print('XL')
        elif i & 16:
            print('XXL')
        elif i & 32:
            print('XXXL')
else:
    print('NO')
