n, s = (list(map(int, input().split())))

buyorder = []
sellorder = []

for i in range(n):
    line = input()
    order = line.split()
    order[1] = int(order[1])
    order[2] = int(order[2])

    if order[0] == "B" :
        for m in buyorder:
            if m[1] == order[1]:
                m[2] += order[2]
                break
        else:
            buyorder.append(order)
    else:
        for m in sellorder:
            if m[1] == order[1]:
                m[2] += order[2]
                break
        else:
            sellorder.append(order)


buyorder.sort(key= lambda data : data[1], reverse = True)
sellorder.sort(key= lambda data : data[1], reverse = False)

if len(sellorder)<s:
    sellorder.sort(key= lambda data : data[1], reverse = True)
    for i in sellorder:
        print(i[0], i[1], i[2])
else:
    newsell = []
    for i in range(s):
        newsell.append(sellorder[i])
    newsell.sort(key= lambda data : data[1], reverse = True)
    for i in range(s):
        print(newsell[i][0], newsell[i][1], newsell[i][2])

if len(buyorder)<s:
    for i in buyorder:
        print(i[0], i[1], i[2])
else:
    for i in range(s):
        print(buyorder[i][0], buyorder[i][1], buyorder[i][2])

