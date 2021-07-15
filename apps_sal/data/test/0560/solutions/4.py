import sys
fin = sys.stdin

n, m = map(int, fin.readline().split())
isRowFree = [True] * n
isColFree = [True] * m

for i in range(n):
    s = fin.readline().strip()
    for j in range(m):
        if s[j] == 'S':
            isRowFree[i] = False
            isColFree[j] = False
      
def FreeRows():
    return sum(1 for i in range(n) if isRowFree[i])
def FreeColumns():
    return sum(1 for i in range(m) if isColFree[i])      

a = FreeRows()
b = FreeColumns()      
      
print(a * m + b * (n - a))
