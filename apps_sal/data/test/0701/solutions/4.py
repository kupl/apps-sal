def yes(listx, desired):
    if len(listx) != len(desired):
        return False
    for char in desired:
        if char in listx:
            listx.remove(char)
        else:
            return False
    return True


def inside(listx, listx2):
    for element in listx2:
        if element in listx:
            ind = listx.index(element)
            listx = listx[ind + 1:]
        else:
            return False
    return True


sa = input()
sa2 = input()
array = 0
auto = 0
saxx = []
saxx2 = []
for char in sa:
    saxx.append(char)
for char in sa2:
    saxx2.append(char)
if sa2 in sa:
    auto = 1
if inside(saxx, saxx2):
    print('automaton')
else:
    saxx.sort()
    saxx2.sort()
    if saxx == saxx2:
        print('array')
    elif inside(saxx, saxx2):
        print('both')
    else:
        print('need tree')
