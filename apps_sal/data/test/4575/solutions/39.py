import sys

n = int(input())
d,x = list(map(int,input().split()))

for i in range(n):
    a = int(input())
    for j in range(1,sys.maxsize,1):
        x += 1
        if a*j+1 > d:
            break
print(x)

