N = int(input())
l = []
for i in range(N):
    l.append(list(map(int, input().split())))

for x in range(101):
    for y in range(101):
        flag = True
        for i in range(N):
            if l[i][2] > 0:
                tmp = abs(x - l[i][0]) + abs(y - l[i][1]) + l[i][2]
                break
        for i in range(N):
            if l[i][2] != max(tmp - abs(x - l[i][0]) - abs(y - l[i][1]), 0):
                flag = False
                break
        if flag:
            print(x, y, tmp)
            return
