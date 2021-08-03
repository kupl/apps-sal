try:
    t = int(input())
    mlist = list(map(int, input().split()))

    for i in range(0, len(mlist)):
        slist = [[1], [2], [4], [3]]
        # print(11111)
        for j in range(0, len(slist)):
            # print(4332)
            for k in range(0, mlist[i] - 1):

                if(j == 0):
                    # print(1)
                    slist[0].append(((slist[0][-1] * 2) + 2))
                if(j == 1):
                    # print(2)
                    slist[1].append(((slist[1][-1] * 2) + 1))
                if(j == 2):
                    # print(3)
                    slist[2].append(((slist[2][-1] * 2) + 2))
                if(j == 3):
                    # print(4)
                    slist[3].append(((slist[3][-1] * 2)))

        for j in range(0, len(slist)):
            # print(5)
            for k in range(0, len(slist[j])):
                print(slist[j][k], end=" ")
            print()
except:
    pass
