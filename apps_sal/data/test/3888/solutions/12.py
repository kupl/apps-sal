# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

sys.setrecursionlimit(10**6)

n = int(readline())
res = [0]*3

a = list(map(int,readline().split()))

mex = [[1,2,1],[2,0,0],[1,0,0]]

def brute(a):
    b = [0]*n
    b[0] = int(readline())
    for i in range(1,n):
        b[i] = mex[a[i]][b[i-1]]
    return b

if n <= 10:
    #print(a)
    for i in a: res[i] += 1
    for _ in range(n-1):
        a = brute(a)        
        for i in a: res[i] += 1
        #print(a)
    print(*res)    
    return


for _ in range(4):
    for i in a: res[i] += 1
    a = brute(a)

for i in range(3):
    res[a[i]] += 1

res[a[3]] += n-4
for i in range(4,n):
    res[a[i]] += n-i

b = a[:4]


for i in range(5,n):
    x = int(readline())
    b[0] = x
    for j in range(1,4):
        res[x] += 1
        x = mex[x][b[j]]
        b[j] = x
    
    #print(x)
    res[x] += n-i


print(*res)
