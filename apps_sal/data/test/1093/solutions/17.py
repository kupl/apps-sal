def getMapH(Map):
    mapHieght = []
    temp = int(0)
    for x in range(len(Map[0])):
        for y in range(len(Map)):

            if(Map[y][x] == "."):
                temp += 1
                continue
            else:
                break
        mapHieght += [len(Map) - temp]
        temp = 0
    return mapHieght


def getMaxdelta(mapH):

    res = int(0)
    for i in range(len(mapH) - 1):
        if(mapH[i + 1] - mapH[i]) > 0:
            res = max(res, mapH[i + 1] - mapH[i])

    return res


def getMindelta(mapH):

    res = int(0)
    for i in range(len(mapH) - 1):
        if(mapH[i] - mapH[i + 1]) > 0:
            res = max(mapH[i] - mapH[i + 1], res)

    return res


inStr = input()
n, m = inStr.split()
# n строк по m символов в каждой
mymap = []
mapHieght = []
for i in range(int(n)):
    inStr = input()
    mymap += [inStr]


print(getMaxdelta(getMapH(mymap)), getMindelta(getMapH(mymap)))
