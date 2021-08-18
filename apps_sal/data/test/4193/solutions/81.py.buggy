lst = [[int(i) for i in input().split()] for j in range(3)]

n = int(input())

for _ in range(n):
    x = int(input())
    for d in lst:
        if d[0] == x:
            d[0] = -1
        elif d[1] == x:
            d[1] = -1
        elif d[2] == x:
            d[2] = -1

for d in lst:
    if d[0] == d[1] == d[2] == -1:
        print('Yes')
        return
for i in range(3):
    if lst[0][i] == lst[1][i] == lst[2][i] == -1:
        print('Yes')
        return
for i in range(3):
    if lst[i][0] == lst[i][1] == lst[i][2] == -1:
        print('Yes')
        return
if lst[0][0] == lst[1][1] == lst[2][2] == -1:
    print('Yes')
    return
if lst[0][2] == lst[1][1] == lst[2][0] == -1:
    print('Yes')
    return
print('No')
