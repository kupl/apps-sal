import math
N = int(input())
ls = []
for i in range(N):
    ls.append(list(map(int,input().split())))

T = 1
A = 1
for i in range(N):
    bai = max(-(-T//ls[i][0]),-(-A//ls[i][1]))
    T = bai * ls[i][0]
    A = bai * ls[i][1]
print(T+A)
