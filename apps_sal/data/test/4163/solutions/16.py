n = int(input())
lst = [input() for _ in range(n)]
x = 0
for i in range(n):
    if x != 3:
        if x == 0 and lst[i][0] == lst[i][2]:
            x = 1
        elif x != 0 and lst[i][0] == lst[i][2]:
            x += 1
        elif x != 0 and lst[i][0] != lst[i][2]:
            x = 0
if x >= 3:
    print('Yes')
else:
    print('No')
