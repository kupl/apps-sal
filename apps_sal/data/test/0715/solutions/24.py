questionNames = ['A', 'B', 'C', 'D']
lengths = [(len(input()) - 2, questionNames[i]) for i in range(4)]
lengths.sort()
firstIsGreat = lengths[0][0] <= lengths[1][0] // 2
lastIsGreat = lengths[3][0] >= lengths[2][0] * 2
if firstIsGreat ^ lastIsGreat:
    if firstIsGreat:
        print(lengths[0][1])
    else:
        print(lengths[3][1])
else:
    print('C')
