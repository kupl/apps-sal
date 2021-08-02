for i in range(int(input())):
    n = int(input())
    s = input()
    d = {}
    x = 0
    y = 0
    d[(x, y)] = [0]
    m1 = -1
    m2 = -1
    c = 0
    for i in s:
        c += 1
        if(i == "L"):
            x -= 1
        elif(i == "R"):
            x += 1
        elif(i == "U"):
            y += 1
        else:
            y -= 1
        try:
            d[(x, y)].append(c)
            if(m1 == -1):
                m2 = d[(x, y)][-1]
                m1 = d[(x, y)][-2]
            if(d[(x, y)][-1] - d[(x, y)][-2]) < (m2 - m1):
                m2 = d[(x, y)][-1]
                m1 = d[(x, y)][-2]
        except:
            d[(x, y)] = [c]
    # print(d)
    if(m1 != -1):
        print(str(m1 + 1) + " " + str(m2))
    else:
        print(-1)
