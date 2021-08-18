Row = int(input())
List = []
for i in range(Row):
    List.append(list(map(int, input().split())))
List = sorted(List, key=lambda x: x[1])
res = 0
flag = True
for i in range(Row):
    res += List[i][0]
    if res > List[i][1]:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")
