for i in range(int(input())):
    a = input()
    b = input()
    di = [[a[0], 1]]
    for i in a[1:]:
        if di[-1][0] == i:
            di[-1][1] += 1
        else:
            di.append([i, 1])
    di2 = [[b[0], 1]]
    for i in b[1:]:
        if di2[-1][0] == i:
            di2[-1][1] += 1
        else:
            di2.append([i, 1])
    if len(di) != len(di2):
        print("NO")
        continue
    f = 0
    for i in range(len(di)):
        if di[i][0] == di2[i][0] and di[i][1] <= di2[i][1]:
            continue
        f = 1
        break
    if f:
        print("NO")
    else:
        print("YES")
