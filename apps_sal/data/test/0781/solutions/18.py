lis = []
for i in range(8):
    lis.append(input())
lis1 = ['WBWBWBWB', 'BWBWBWBW']
check = 1
for i in range(8):
    if lis[i] not in lis1:
        check = 0
if check == 0:
    print('NO')
else:
    print('YES')
