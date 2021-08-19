Row = int(input())
List = []
for i in range(Row):
    List.append(list(map(int, input().split())))
x = 0
y = 0
T = 0
flag = True
for i in range(Row):
    reqT = abs(List[i][1] - x) + abs(List[i][2] - y)
    chck = List[i][0] - T - reqT
    if chck < 0 or chck % 2 == 1:
        flag = False
        break
    x = List[i][1]
    y = List[i][2]
    T = List[i][0]
if flag:
    print('Yes')
else:
    print('No')
