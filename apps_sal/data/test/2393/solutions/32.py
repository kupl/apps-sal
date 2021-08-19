t = int(input())
for i in range(t):
    s = input()
    one, twone = 0, 0
    a = []
    for j in range(len(s)):
        st = s[j]
        if twone == 0 and st == 't':
            twone = 1
        elif twone == 1 and st == 'w':
            twone = 2
        elif twone == 2 and st == 'o':
            twone = 3
        elif twone == 3 and st == 'n':
            twone = 4
        elif twone == 4 and st == 'e':
            twone = 5
        else:
            if twone == 5:
                a.append(j - 2)
            elif twone >= 3:
                a.append(j - twone + 2)
            twone = 0
            if st == 't':
                twone = 1
        if twone != 3:
            if one == 0 and st == 'o':
                one = 1
            elif one == 1 and st == 'n':
                one = 2
            elif one == 2 and st == 'e':
                one = 3
            else:
                if one == 3:
                    a.append(j - 1)
                one = 0
                if st == 'o':
                    one = 1
        # print(one,twone,j,st,a)
    if twone == 5:
        a.append(j - 1)
    elif twone >= 3:
        a.append(j - twone + 4)
    if one == 3:
        a.append(j)
    print(len(a))
    print(*a)
