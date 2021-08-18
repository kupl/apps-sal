list2 = []
for i in range(4):
    list1 = list(map(int, input().strip().split(' ')))
    list2.append(list1)
if list2[0][3] == 1:
    if list2[1][0] == 1 or list2[2][1] == 1 or list2[3][2] == 1 or list2[0][1] == 1 or list2[0][2] == 1 or list2[0][0] == 1:
        print("YES")
        return
if list2[1][3] == 1:
    if list2[0][2] == 1 or list2[2][0] == 1 or list2[3][1] == 1 or list2[1][1] == 1 or list2[1][2] == 1 or list2[1][0] == 1:
        print("YES")
        return
if list2[2][3] == 1:
    if list2[0][1] == 1 or list2[1][2] == 1 or list2[3][0] == 1 or list2[2][1] == 1 or list2[2][2] == 1 or list2[2][0] == 1:
        print("YES")
        return
if list2[3][3] == 1:
    if list2[0][0] == 1 or list2[1][1] == 1 or list2[2][2] == 1 or list2[3][1] == 1 or list2[3][2] == 1 or list2[3][0] == 1:
        print("YES")
        return
print("NO")
