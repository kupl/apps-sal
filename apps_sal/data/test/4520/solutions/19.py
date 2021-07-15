scount, badness = [int(x) for x in input().split(' ')]
segments = []
length = 200
for i in range(scount):
    segments.append([int(x) - 1 for x in input().split(' ')])
    segments[-1].append(True)
array = [[] for x in range(length)]
badcheck = [0 for x in range(length)]
for i in range(scount):
    for k in range(segments[i][0], segments[i][1] + 1):
        array[k].append([segments[i][1], i])
        badcheck[k] += 1
for i in range(length):
    array[i].sort()
res = []
for i in range(length):
    while badcheck[i] > badness:
        fn = array[i].pop()
        while not segments[fn[1]][2] == True:
            fn = array[i].pop()
        segments[fn[1]][2] = False
        res.append(fn[1])
        for k in range(i, fn[0] + 1):
            badcheck[k] -= 1
res.sort()
printable = ''
for i in res:
    printable += str(i + 1) + ' '
print(len(res))
print(printable)
