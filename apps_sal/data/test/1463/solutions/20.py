def fin(s, row, column):
    for i in row:
        for j in column:
            if i + j == s:
                return True
    return False


n = int(input())
a = []
for i in range(n):
    k = input().split(' ')
    k = list(map(int, k))
    a.append(k)
ans = True
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            continue
        else:
            s = a[i][j]
            row = a[i]
            column = []
            for t in range(n):
                column.append(a[t][j])
            ans = fin(s, row, column)
            if ans == False:
                break
    if ans == False:
        break
if ans == True:
    print('Yes')
else:
    print('No')
