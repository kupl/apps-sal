import sys

n = int(input())
B = [list(input()) for _ in range(n)]

def ok(x,y):
    return 0 <= x < n and 0 <= y < n

def try_add(i,j):
    if ok(i,j) and B[i][j] == '.':
        B[i][j] = '#'
        return True
    return False

def add_plus(i,j):
    if not try_add(i,j): return False
    if not try_add(i+1,j): return False
    if not try_add(i+2,j): return False
    if not try_add(i+1,j-1): return False
    if not try_add(i+1,j+1): return False
    return True

for i in range(n):
    for j in range(n):
        if B[i][j] == '.':
            if not add_plus(i,j):
                print('NO')
                return
print('YES')

