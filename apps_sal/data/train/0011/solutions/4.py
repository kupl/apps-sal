for q in range(int(input())):

    data = input()
    # if data in ["WW", "AA", "SS", "DD"]:
    #     print(2)
    #     continue
    mx = [0,0,0,0]
    x = 0
    y = 0
    pos = [[-1],[-1],[-1],[-1]]
    for i in range(len(data)):
        # print(x,y)
        d = data[i]
        if d == "W":
            y += 1
            if y > mx[0]:
                
                mx[0] = y
                pos[0] = []
        elif d == "S":
            y -= 1
            if y < mx[2]:
                
                mx[2] = y
                pos[2] = []
        elif d == "A":
            x -= 1
            if x < mx[1]:
                
                mx[1] = x
                pos[1] = []
        else:
            x += 1
            if x > mx[3]:
                
                mx[3] = x
                pos[3] = []
        if x == mx[3]:
            pos[3].append(i)
        if x == mx[1]:
            pos[1].append(i)
        if y == mx[0]:
            pos[0].append(i)
        if y == mx[2]:
            pos[2].append(i)

    # print(mx)
    # print(pos)
    wid = mx[3] - mx[1] + 1
    hei = mx[0] - mx[2] + 1
    ans = wid * hei

    
    
    if pos[3][0] > pos[1][-1] + 1 or pos[1][0] > pos[3][-1] + 1:
        ans -= hei
    if pos[0][0] > pos[2][-1] + 1 or pos[2][0] > pos[0][-1] + 1:
        ans = min((hei-1)*(wid), ans)
    print(ans)
