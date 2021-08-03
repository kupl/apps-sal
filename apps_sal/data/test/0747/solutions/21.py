nw = input().split()
numCandies = int(nw[0])
weight = int(nw[1])

thm1 = []
thm2 = []

for i in range(numCandies):
    val = input().split()
    val = [int(x) for x in val]
    if val[0] == 0:
        thm1.append(val)
    else:
        thm2.append(val)


def get_candy(woc, tlist):
    ind = -1
    maxm = -1
    for k in range(len(tlist)):
        if tlist[k][1] <= woc:
            if maxm < tlist[k][2]:
                maxm = tlist[k][2]
                ind = k
    if ind >= 0:
        val1 = tlist.pop(ind)
        return val1
    return None


count = [0, 0]
for i in range(2):
    candyType = i
    initialWeight = weight
    thm1c = thm1[:]
    thm2c = thm2[:]
    while True:
        if candyType == 0:
            candy = get_candy(initialWeight, thm1c)
            if candy is not None:
                chm = candy
                h = chm[1]
                m = chm[2]
                initialWeight += m
                count[i] += 1
                candyType = 1
            else:
                break
        else:
            candy = get_candy(initialWeight, thm2c)
            if candy is not None:
                chm = candy
                h = chm[1]
                m = chm[2]
                initialWeight += m
                count[i] += 1
                candyType = 0
            else:
                break
print(max(count))
