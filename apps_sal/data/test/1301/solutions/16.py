n = int(input())
clue = str(input())
namelist = ['jolt', 'flar', 'umbr', 'leaf', 'glac', 'sylv']
notname = []
if n == 8:
    print('vaporeon')
    quit()
if n == 6:
    print('espeon')
    quit()
clue = clue[:-3]
for i in range(4):
    for name in namelist:
        if name not in notname:
            if clue[i] != '.' and clue[i] != name[i]:
                notname.append(name)
for name in namelist:
    if name not in notname:
        print(name + 'eon')
        quit()
