num = int(input())
flag = False
balls = []
for x in input().split(" "):
    balls.append(int(x))

balls.sort()
cont = 1
for i in range(0, num - 1):
    j = i + 1
    m = i + 2
    if(balls[i] == balls[j]):
        m += 1
    elif((balls[j] - balls[i] <= 1) and (balls[i] != balls[j])):
        cont += 1
    else:
        cont = 1
    # print(cont)
    if(cont == 3):
        flag = True
        break


if(flag):
    print("YES")
else:
    print("NO")
##print("%d %d %d"%(balls[i],balls[j],balls[m]))
