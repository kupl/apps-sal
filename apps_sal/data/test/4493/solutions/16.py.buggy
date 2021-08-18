List = [list(map(int, input().split())) for i in range(3)]
newlist = []
new = [x - y for (x, y) in zip(List[0], List[1])]
new2 = [x - y for (x, y) in zip(List[2], List[1])]
if new[0] == new[1] and new[1] == new[2]:
    pass
else:
    print('No')
    return
if new2[0] == new2[1] and new2[1] == new2[2]:
    pass
else:
    print('No')
    return

if List[0][0] - List[0][1] == List[1][0] - List[1][1] and List[2][0] - List[2][1] == List[1][0] - List[1][1]:
    pass
else:
    print('No')
    return
if List[0][0] - List[0][2] == List[1][0] - List[1][2] and List[2][0] - List[2][2] == List[1][0] - List[1][2]:
    pass
else:
    print('No')
    return
print('Yes')
