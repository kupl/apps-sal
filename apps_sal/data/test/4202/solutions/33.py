import sys


l,r=map(int,input().split())

k=2020
if r-l>=2020:
    print(0)
    return
else:
    for i in range(l,r):
        for j in range(i+1,r+1):
            k=min(k,(i*j)%2019)
print(k)
