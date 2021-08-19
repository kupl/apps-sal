Inpt = int(input())
Mainlist = sorted(list(map(int, input().split(' '))))
Score = 0
if Inpt == 1:
    print(int(Mainlist[0]))
elif Inpt == 2:
    print(2 * (int(Mainlist[1]) + int(Mainlist[0])))
else:
    for i in range(len(Mainlist)):
        Score += (i + 2) * int(Mainlist[i])
    Score -= int(Mainlist[Inpt - 1])
    print(Score)
