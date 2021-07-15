import os
import sys
import io

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline # 神奇快读，无法运行调试
GANS = []

# def print(*args): # 神奇快写，最后得写上os.write
#     nonlocal GANS
#     for i in args:
#         GANS.append(f'{i}'.encode())


t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    li = [int(i) for i in input().split()]
    d1 = {}
    d2 = {}
    col = []
    for i in li:
        if d1.get(k-i,0) > d2.get(k-i,0):
            d2[i] = d2.get(i,0) + 1
            col.append(1)
        else:
            d1[i] = d1.get(i,0) + 1
            col.append(0)
    print(*col)
