import copy
n, xx = map(int, input().split())
firstorig = list()
secondorig = list()
for i in range(n):
    t, h, m = map(int, input().split())
    if t == 0:
        firstorig.append((h, m))
    else:
        secondorig.append((h, m))

#print(len(firstorig), len(secondorig))
firstres = 0
first = copy.deepcopy(firstorig)
second = copy.deepcopy(secondorig)
curmaxjump = xx

while True:
    #print(len(first), len(second), firstres)
    if len(first) > 0:
        i = 0
        weight = 0
        for x in range(len(first)):
            if first[x][0] <= curmaxjump and first[x][1] > weight:
                weight = first[x][1]
                i = x
        if weight > 0:
            firstres += 1
            curmaxjump += weight
            first.pop(i)
        else:
            break
    else:
        break
    if len(second) > 0:
        i = 0
        weight = 0
        for x in range(len(second)):
            if second[x][0] <= curmaxjump and second[x][1] > weight:
                weight = second[x][1]
                i = x
        if weight > 0:
            firstres += 1
            curmaxjump += weight
            second.pop(i)
        else:
            break
    else:
        break

secondres = 0
curmaxjump = xx
first = copy.deepcopy(firstorig)
second = copy.deepcopy(secondorig)

while True:
    #print(len(first), len(second), curmaxjump)
    if len(second) > 0:
        i = 0
        weight = 0
        for x in range(len(second)):
            if second[x][0] <= curmaxjump and second[x][1] > weight:
                weight = second[x][1]
                i = x
        if weight > 0:
            secondres += 1
            curmaxjump += weight
            second.pop(i)
        else:
            break
    else:
        break
    #print(len(first), len(second), firstres)
    if len(first) > 0:
        i = 0
        weight = 0
        for x in range(len(first)):
            if first[x][0] <= curmaxjump and first[x][1] > weight:
                weight = first[x][1]
                i = x
        if weight > 0:
            secondres += 1
            curmaxjump += weight
            first.pop(i)
        else:
            break
    else:
        break


# print(firstres)
#print(firstres, secondres)
print(max(firstres, secondres))
