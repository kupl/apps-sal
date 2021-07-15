
def c(i, j):
    if i < 4 and j < 4 and i >= 0 and j >= 0:
        if a[i][j] == 'x':
            return True
    return False

a = [[x for x in input().strip()] for j in range(4)]
ans = True
for i in range(4):
    for j in range(4):
        if a[i][j] == '.':
            if c(i+1,j) and c(i+2,j):
                ans = False
            if c(i-1,j) and c(i-2,j):
                ans = False
            if c(i+1,j+1) and c(i+2,j+2):
                ans = False
            if c(i-1,j-1) and c(i-2,j-2):
                ans = False
            if c(i,j+1) and c(i,j+2):
                ans = False
            if c(i,j-1) and c(i,j-2):
                ans = False
            if c(i+1,j-1) and c(i+2,j-2):
                ans = False
            if c(i-1,j+1) and c(i-2,j+2):
                ans = False

            if c(i-1,j-1) and c(i+1,j+1):
                ans = False
            if c(i-1,j) and c(i+1,j):
                ans = False
            if c(i-1,j+1) and c(i+1,j-1):
                ans = False
            if c(i,j-1) and c(i,j+1):
                ans = False

if ans:
    print('NO')
else:
    print('YES')
