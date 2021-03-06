import heapq
MAXEN = 2 * 10 ** 5 + 5
(N, Q) = list(map(int, input().split()))
kid = [0]
en = [0]
entop = [[] for _ in range(MAXEN)]
alltop = []
addAllList = []
rmvAllList = []
for i in range(N):
    (a, b) = list(map(int, input().split()))
    kid.append(a)
    en.append(b)
    heapq.heappush(entop[b], -a)
for e in range(MAXEN):
    if entop[e]:
        vv = entop[e][0]
        heapq.heappush(alltop, -vv)
addlist = [[] for _ in range(MAXEN)]
rmvlist = [[] for _ in range(MAXEN)]


def updateEn(enID):
    while len(addlist[enID]) > 0:
        add_top = addlist[enID][0]
        needAddNow = True
        if len(rmvlist[enID]) > 0:
            needAddNow = True
        elif entop[enID]:
            entop_old = entop[enID][0]
            needAddNow = add_top < entop_old
        if needAddNow:
            heapq.heappush(entop[enID], add_top)
            heapq.heappop(addlist[enID])
        else:
            break
    while len(entop[enID]) > 0 and len(rmvlist[enID]) > 0:
        rmv_top = rmvlist[enID][0]
        entop_old = entop[enID][0]
        if rmv_top == entop_old:
            heapq.heappop(entop[enID])
            heapq.heappop(rmvlist[enID])
        else:
            break


for q in range(Q):
    (c, d) = list(map(int, input().split()))
    old_en = en[c]
    new_en = d
    en[c] = new_en
    heapq.heappush(rmvlist[old_en], -kid[c])
    heapq.heappush(addlist[new_en], -kid[c])
    if len(entop[old_en]) > 0:
        entop_old0 = entop[old_en][0]
    else:
        entop_old0 = 0
    if len(entop[new_en]) > 0:
        entop_new0 = entop[new_en][0]
    else:
        entop_new0 = 0
    updateEn(new_en)
    updateEn(old_en)
    if len(entop[old_en]) > 0:
        entop_old1 = entop[old_en][0]
    else:
        entop_old1 = 0
    if entop_old0 != entop_old1:
        if entop_old0 != 0:
            heapq.heappush(rmvAllList, -entop_old0)
        if entop_old1 != 0:
            heapq.heappush(addAllList, -entop_old1)
    if len(entop[new_en]) > 0:
        entop_new1 = entop[new_en][0]
    else:
        entop_new1 = 0
    if entop_new0 != entop_new1:
        if entop_new0 != 0:
            heapq.heappush(rmvAllList, -entop_new0)
        if entop_new1 != 0:
            heapq.heappush(addAllList, -entop_new1)
    while len(addAllList) > 0:
        add_top = addAllList[0]
        if len(alltop) == 0 or add_top < alltop[0] or len(rmvAllList) > 0:
            heapq.heappush(alltop, add_top)
            heapq.heappop(addAllList)
        else:
            break
    while len(rmvAllList) > 0:
        rmvTopV = rmvAllList[0]
        if rmvTopV == alltop[0]:
            heapq.heappop(alltop)
            heapq.heappop(rmvAllList)
        else:
            break
    print(alltop[0])
