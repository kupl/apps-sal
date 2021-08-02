List = []
for i in range(3):
    List.append(list(map(int, input().split())))
a = 0
b = 0
c = 0
flg = True
for i in range(2):
    a = List[0][i + 1] - List[0][i]
    b = List[1][i + 1] - List[1][i]
    c = List[2][i + 1] - List[2][i]
    if a != b or b != c or c != a:
        flg = False
    a = List[i + 1][0] - List[i][0]
    b = List[i + 1][1] - List[i][1]
    c = List[i + 1][2] - List[i][2]
    if a != b or b != c or c != a:
        flg = False
if flg:
    print("Yes")
else:
    print("No")
