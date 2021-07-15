
t = int(input())

for loop in range(t):

    n = int(input())
    xy = []
    ans = []

    for i in range(n):

        x,y = list(map(int,input().split()))
        xy.append([x,y])

    xy.sort()

    x = 0
    y = 0
    flag = True

    for i in range(n):
        nexx = xy[i][0]
        nexy = xy[i][1]

        if x > nexx or y > nexy:
            flag = False
            break

        while x < nexx:
            ans.append("R")
            x += 1

        while y < nexy:
            ans.append("U")
            y += 1

    if flag:
        print ("YES")
        print("".join(ans))
    else:
        print ("NO")

