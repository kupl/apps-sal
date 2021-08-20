import math
n = int(input())
columns = list(map(int, input().rstrip().split()))
modcolumns = [i % 2 for i in columns]
test = 0
previouslist = []
for i in range(0, n):
    if len(previouslist) == 0:
        previouslist.append(modcolumns[i])
    elif modcolumns[i] == previouslist[-1]:
        previouslist.pop()
    else:
        previouslist.append(modcolumns[i])
if len(previouslist) <= 1:
    print('YES')
else:
    print('NO')
