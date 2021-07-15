n, m, k = map(int, input().split())

def printTube(tube):
    print(len(tube), end=' ')
    for cell in tube:
        print(cell[0] + 1, cell[1] + 1, end=' ')
    print()

nbTubes = 0
currTube = []
for i in range(n):
    if i % 2 == 0:
        jDomain = range(m)
    else:
        jDomain = reversed(range(m))

    for j in jDomain:
        currTube.append((i, j))
        if len(currTube) >= 2 and nbTubes < k-1:
            printTube(currTube)
            currTube = []
            nbTubes += 1
printTube(currTube)
