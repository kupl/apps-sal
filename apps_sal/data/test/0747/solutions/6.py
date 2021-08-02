def solve(currentT):
    result = 0
    way = list(candy)
    bestCandy = -1
    flag = False
    for i in range(n):
        if way[i][0] == currentT:
            if way[i][1] <= x and (way[i][2] >= way[bestCandy][2] or bestCandy == -1):
                bestCandy = i
                flag = True
    if not flag:
        return 0
    power = x + way[bestCandy][2]
    result += 1
    flag = True
    while flag:
        temp = way.pop(bestCandy)
        bestCandy = -1
        currentT = 1 - currentT
        flag = False
        for i in range(len(way)):
            if way[i][0] == currentT:
                if way[i][1] <= power and (way[i][2] >= way[bestCandy][2] or bestCandy == -1):
                    bestCandy = i
                    flag = True
        if flag:
            power += way[bestCandy][2]
            result += 1
    return result


candy = []
n, x = tuple(map(int, input().split()))
for i in range(n):
    temp = list(map(int, input().split()))
    if temp[0] > 0:
        temp[0] = 1
    candy.append(temp)
candy = tuple(candy)

print(max(solve(0), solve(1)))
