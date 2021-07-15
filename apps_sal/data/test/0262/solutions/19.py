import sys
n = int(input())
mat = []
empty = (None, None)
if n == 1:
    print(1)
    return
for i in range(n):
    row = [int(x) for x in input().strip().split()]
    if 0 in row:
        col = row.index(0)
        empty = (i, col)
    mat.append(row)
i = 0
if 0 in mat[i]:
    i += 1
rowsum = sum(mat[i])
row = empty[0]
for i in range(n):
    if i == row:
        continue
    cursum = sum(mat[i])
    # print(cursum)
    if cursum != rowsum:
        print(-1)
        return
tmat = list(zip(*mat))
col = empty[1]
for i in range(n):
    if i == col:
        continue
    else:
        #print(cursum)
        cursum = sum(tmat[i])
        if cursum != rowsum:
            print(-1)
            return
row = empty[0]
irowsum = sum(mat[row])
colsum = sum(tmat[col])
#print(irowsum, colsum)
if irowsum != colsum:
    print(-1)
    return
left = 0
right = 0
tochange = rowsum - irowsum
if tochange <= 0:
    print(-1)
    return
mat[row][col] = tochange
if True:
    for i in range(n):
        #print(mat[i][i], mat[i][n - i - 1])
        left += mat[i][i]
        right += mat[i][n - i - 1]
    #print(left, right)
    #print(row, col, left, rowsum)
if left != right or left != rowsum:
    print(-1)
    return
print(tochange)

