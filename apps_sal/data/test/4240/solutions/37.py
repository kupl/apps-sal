import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

s = input()
t = input()
n = len(s)

for i in range(n):
    flag = 0
    for j in range(n):
        if s[(i+j)%n] != t[j]:
            flag = 1
            break
    if flag == 0:
        print('Yes')
        return
print('No')
