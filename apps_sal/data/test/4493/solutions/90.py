xy = [list(map(int, input().split())) for i in range(3)]
result = sum(map(sum, xy))
if result % 3 != 0:
    print("No")
    return
if result != (xy[0][0]+xy[1][1]+xy[2][2]) * 3:
    print("No")
    return
if result != (xy[0][2]+xy[1][1]+xy[2][0]) * 3:
    print("No")
    return
else:
    print("Yes")
