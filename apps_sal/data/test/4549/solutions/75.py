col,row = [int(x) for x in input().split()]
map_list = [[0] * (row+2)]
for i in range(col):
    map_list.append(["0"] + list(input()) + ["0"])
map_list.append(map_list[0])
#print(map_list)

def check(x,y):
    lands = [[x,y]]
    #print(lands)
    area = 0
    sealine = 0
    while lands:
        #print(area)
        #print(lands)
        x,y = lands.pop()
        #print(x,y)
        area += 1
        map_list[y][x] = "2"
        if map_list[y+1][x] == "#":
            lands.append([x,y+1])
        elif not map_list[y+1][x] == "2":
            sealine += 1
        if map_list[y][x+1] == "#":
            lands.append([x+1,y])
        elif not map_list[y][x+1] == "2":
            sealine += 1
        if map_list[y-1][x] == "#":
            lands.append([x,y-1])
        elif not map_list[y-1][x] == "2":
            sealine += 1
        if map_list[y][x-1] == "#":
            lands.append([x-1,y])
        elif not map_list[y][x-1] == "2":
            sealine += 1
        lands = list(map(tuple,lands))
        lands = list(set(lands))
        #print(lands)
    return area

res = "Yes"
for i in range(1,col+1):
    for j in range(1,row+1):
        if map_list[i][j] == "#":
            if check(j,i) == 1:
              res = "No"
print(res)
