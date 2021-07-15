from sys import stdin

def generator(k):
    nonlocal generation
    nonlocal resnum
    nonlocal a
    if(k == 5):
        sm = a[generation[0]][generation[1]] + a[generation[1]][generation[0]] + 2 * a[generation[2]][generation[3]] + 2 * a[generation[3]][generation[2]] + a[generation[1]][generation[2]] + a[generation[2]][generation[1]] + 2 * a[generation[3]][generation[4]] + 2 * a[generation[4]][generation[3]]
        if(sm > resnum):
            resnum = sm
    else:
        for i in range(5):
            if not(i in generation):
                generation[k] = i
                generator(k + 1)
                generation[k] = -1


a = []
for i in range(5):
    a.append(list(map(int, stdin.readline().split())))
print()
generation = [-1 for i in range(5)]
resnum = -1
generator(0)
print(resnum)
