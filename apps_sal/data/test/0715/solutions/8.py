answerlist = []
lengthlist = []
great = 0
finallist = ['A', 'B', 'C', 'D']
for i in range(4):
    answerlist.append(str(input()))
    lengthlist.append(len(answerlist[i]) - 2)

lengthlist1 = lengthlist[:]
lengthlist.sort()

if lengthlist[0] * 2 <= lengthlist[1]:
    great = 1
if lengthlist[3] >= lengthlist[2] * 2:
    if great == 1:
        great = 0
    else:
        great = 2
if great == 0:
    print('C')
if great == 1:
    print(finallist[lengthlist1.index(lengthlist[0])])
if great == 2:
    print(finallist[lengthlist1.index(lengthlist[3])])
