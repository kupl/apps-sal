n = int(input())
coors = []
for i in range(n):
    coors.append(list(map(int, input().split())) + [i + 1])
# print(coors)
coors = sorted(coors, key=lambda x: (x[0], x[1], x[2]))
# for i in range(0,n,2):
#     if coors[i][0]==coors[i+1][0]:
#         if coors[i][1]==coors[i+1][1]:
#             print(coors[i][3],coors[i+1][3])
#         else:
left = []


def oneD(co, remain):
    if len(co) % 2 == 0:
        for i in range(0, len(co), 2):
            print(co[i][3], co[i + 1][3])
    else:
        remain.append(co[-1])
        for i in range(0, len(co) - 1, 2):
            print(co[i][3], co[i + 1][3])
    return remain


def twoD(co):
    if len(co) == 1:
        left.append(*co)
        return
    remain = []
    l = 1
    for i in range(len(co) - 1):
        if co[i][1] == co[i + 1][1]:
            l += 1
        else:
            remain = oneD(co[i + 1 - l:i + 1], remain)
            l = 1
    remain = oneD(co[len(co) - l:], remain)
    if len(remain) % 2 == 0:
        for i in range(0, len(remain), 2):
            print(remain[i][3], remain[i + 1][3])
    else:
        left.append(remain[-1])
        for i in range(0, len(remain) - 1, 2):
            print(remain[i][3], remain[i + 1][3])


l = 1
for i in range(n - 1):
    if coors[i][0] == coors[i + 1][0]:
        l += 1
    else:
        twoD(coors[i + 1 - l:i + 1])
        l = 1
twoD(coors[n - l:])
# print(left)
for i in range(0, len(left), 2):
    print(left[i][3], left[i + 1][3])
