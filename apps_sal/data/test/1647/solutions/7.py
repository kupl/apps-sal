parent = [i for i in range(200)]

def fin (x):
    if parent[x] == x:
        return x
    x = parent[x]
    parent[x] = fin(x)
    return parent[x]


#import sys
#sys.stdin = open ('464-D.in', 'r')

n = int(input())
a = input()
b = input()
lst = []
for i in range(0,n):
    x = ord(a[i])-48
    y = ord(b[i])-48
    u = fin(x)
    v = fin(y)
    if u!=v:
        lst.append((ord(a[i])-48,ord(b[i])-48))
        parent[u] = v

print(len(lst))
for i, j in lst:
    print (chr(i+48), chr(j+48))
